from src.domain.entities.enums import ACCESS_LEVEL
from src.domain.entities.user import User
from src.domain.errors.errors import NonExistentUser, InvalidCredentials
from src.domain.repositories.user_repository_interface import IUserRepository
from src.domain.usecases.check_token_usecase import CheckTokenUsecase


class ListUsersUsecase:

    def __init__(self, userRepository: IUserRepository):
        self._userRepository = userRepository
        self.mutatable_fields = ['name', 'ra', 'year', 'course', 'image']

    async def __call__(self, userList: list, accessToken: str):
        checkTokenUsecase = CheckTokenUsecase(self._userRepository)
        try:
            userRequester = User.parse_obj(await checkTokenUsecase(accessToken))

            allUsers = await self._userRepository.getAllUsers()
            userDict = {}
            for user in allUsers:
                if user.ra in userList:
                    userDict[user.ra] = user.dict()

            if len(userDict) != len(userList):
                for ra in userList:
                    if ra not in userDict.keys():
                        userDict[ra] = {"error": f"User not found"}

            return userDict

        except NonExistentUser as error:
            raise NonExistentUser(error.message)


