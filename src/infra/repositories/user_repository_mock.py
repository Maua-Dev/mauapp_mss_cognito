from datetime import datetime
from typing import List

from src.domain.entities.enums import ROLE, ACCESS_LEVEL
from src.domain.entities.user import User
from src.domain.errors.errors import UnexpectedError
from src.domain.repositories.user_repository_interface import IUserRepository


class UserRepositoryMock(IUserRepository):
    def __init__(self) -> None:
        super().__init__()
        self._users = [
            User(name='user1', cpfRne=12345678910, ra=19003315, role=ROLE.STUDENT,
                 accessLevel=ACCESS_LEVEL.USER, createdAt=datetime(2022, 3, 8, 22, 10),
                 updatedAt=datetime(2022, 3, 8, 22, 15), email="bruno@bruno.com"
             ),
            User(name='user2', cpfRne=12345678911, ra=20001231, role=ROLE.PROFESSOR,
                 accessLevel=ACCESS_LEVEL.ADMIN, createdAt=datetime(2022, 2, 15, 23, 15),
                 updatedAt=datetime(2022, 2, 15, 23, 15)
             )
        ]

    def getAllUsers(self) -> List[User]:
        if len(self._users) > 0:
            return self._users, len(self._users)
        else:
            return None, 0

    async def getUserByCpfRne(self, cpfRne: int) -> User:
        user: User = None
        for userx in self._users:
            if userx.cpfRne == cpfRne:
                user = userx
        return user

    async def checkUserByPropriety(self, propriety: str, value: str) -> bool:
        for userx in self._users:
            if getattr(userx, propriety) == value and value != None:
                return True
        return False

    async def createUser(self, user: User):
        self._users.append(user)

    async def updateUser(self, user: User):
        cont = 0
        for userx in self._users:
            if userx.cpfRne == user.cpfRne:
                break
            cont += 1

        self._users[cont] = user

    async def deleteUser(self, cpfRne: int):
        cont = 0
        for userx in self._users:
            if userx.cpfRne == cpfRne:
                self._users.pop(cont)
                break
            cont += 1
