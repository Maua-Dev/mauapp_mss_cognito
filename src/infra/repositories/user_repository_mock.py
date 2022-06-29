from datetime import datetime
from typing import List

from src.domain.entities.enums import ROLE, ACCESS_LEVEL, YEAR_ENUM
from src.domain.entities.user import User
from src.domain.errors.errors import UnexpectedError, InvalidToken, UserAlreadyExists, InvalidCode, NonExistentUser, \
    UserAlreadyConfirmed
from src.domain.repositories.user_repository_interface import IUserRepository


class UserRepositoryMock(IUserRepository):

    def __init__(self) -> None:
        super().__init__()
        self._users = [
            User(id="123", name='Bruno Vilardi', ra=19003315, year=YEAR_ENUM._4,
                 courseCode="ECM", image="www.link.com.br"
                 ),
            User(id="345", name='Hector Ronaldo', ra=12345678, year=YEAR_ENUM._3,
                 courseCode="ECM", image="www.link.com.br"
                 ),
            User(id="678", name='Johny White', ra=87654321, year=YEAR_ENUM._5,
                 courseCode="ECM", image="www.link.com.br"
                 )
        ]
        self._confirmedUsers = [
            self._users[0],
            self._users[1]
        ]

    async def getAllUsers(self) -> List[User]:
        if len(self._confirmedUsers) > 0:
            return self._confirmedUsers
        else:
            return None

    async def getUserByRA(self, RA: str) -> User:
        user: User = None
        for userx in self._confirmedUsers:
            if userx.ra == RA:
                user = userx
                break
            pass
        return user

    async def checkUserByPropriety(self, propriety: str, value: str) -> bool:
        for userx in self._users:
            if getattr(userx, propriety) == value and value != None:
                return True
        return False

    async def createUser(self, user: User):
        duplicitySensitive = ['ra']
        for field in duplicitySensitive:
            if await self.checkUserByPropriety(propriety=field, value=getattr(user, field)):
                raise UserAlreadyExists(f'Propriety ${field} = "${getattr(user, field)}" already exists')
        self._users.append(user)

    async def confirmUserCreation(self, login: str, code: int) -> bool:
        # code = 1234567

        if code != "1234567":
            raise InvalidCode(f'Invalid code')
        user: User = None
        for userx in self._users:
            if userx.ra == login:
                user = userx
                break
        if not user:
            raise NonExistentUser(f'User not found')
        if userx in self._confirmedUsers:
            raise UserAlreadyConfirmed(f'User already confirmed')
        self._confirmedUsers.append(user)
        return True


    async def updateUser(self, user: User):
        cont = 0
        for userx in self._confirmedUsers:
            if userx.ra == user.ra:
                break
            cont += 1

        self._confirmedUsers[cont] = user

    async def deleteUser(self, ra: str):
        cont = 0
        for userx in self._confirmedUsers:
            if userx.ra == ra:
                self._confirmedUsers.pop(cont)
                break
            cont += 1

    async def loginUser(self, ra: str, password: str) -> dict:
        u = await self.getUserByRA(ra)
        if u is None:
            return None
        if u.password == password:
            dictResponse = u.dict()
            dictResponse.pop('password')
            dictResponse["accessToken"] = "validAccessToken-" + str(ra)
            dictResponse["refreshToken"] = "validRefreshToken-" + str(ra)
            return dictResponse
        return None

    async def checkToken(self, token: str) -> dict:
        splitToken = token.split("-")
        if len(splitToken) != 2:
            return None
        if splitToken[0] != "validAccessToken":
            return None

        ra = splitToken[1]
        user = await self.getUserByRA(ra)
        if user is None:
            return None
        data = user.dict()
        data.pop('password')
        return data

    async def refreshToken(self, refreshToken: str) -> (str, str):
        splitToken = refreshToken.split("-")  # token, cpf
        if len(splitToken) != 2:
            return None, None
        if splitToken[0] != "validRefreshToken":
            return None, None
        if await self.getUserByRA(splitToken[1]) is None:
            return None, None
        return "validAccessToken-" + splitToken[1], refreshToken

    async def changePassword(self, login: str) -> bool:
        user = None
        if login.isdigit():
            user = await self.getUserByRA(login)
        if user:
            return True

        for userx in self._confirmedUsers:
            if userx.email == login:
                return True
        return False



    async def confirmChangePassword(self, login: str, newPassword: str, code: str) -> bool:
        # code = 123456

        # Check code
        if code != "123456":
            return False

        # Update user password
        user = None
        if login.isdigit():
            user = await self.getUserByRA(login)
        if user:
            user.password = newPassword
            return True
        for userx in self._confirmedUsers:
            if userx.email == login:
                userx.password = newPassword
                return True
        return False

    async def resendConfirmationCode(self, ra: str) -> bool:
        user = await self.getUserByRA(ra)

        if user is None:
            raise NonExistentUser(f"{ra}")

        # Send email

        return True



