from src.domain.entities.user import User
from src.domain.errors.errors import UserAlreadyExists, UnexpectedError, NoItemsFound, NonExistentUser
from src.domain.repositories.user_repository_interface import IUserRepository
from src.domain.usecases.get_user_by_ra_usecase import GetUserByRAUsecase


class DeleteUserUsecase:

    def __init__(self, userRepository: IUserRepository):
        self._userRepository = userRepository

    async def __call__(self, ra: int):
        try:
            # Check if immutable fields are changed
            GetUserByRAUC = GetUserByRAUsecase(self._userRepository)
            await GetUserByRAUC(ra)

            await self._userRepository.deleteUser(ra)

        except (NoItemsFound, NonExistentUser) as error:
            raise NonExistentUser(error.message)


