from src.domain.entities.user import User
from src.domain.errors.errors import UserAlreadyExists, UnexpectedError, NoItemsFound, NonExistentUser
from src.domain.repositories.user_repository_interface import IUserRepository
from src.domain.usecases.get_user_by_id_usecase import GetUserByIdUsecase


class DeleteUserUsecase:

    def __init__(self, userRepository: IUserRepository):
        self._userRepository = userRepository

    async def __call__(self, id: int):
        try:
            # Check if immutable fields are changed
            getUserByIDRneUsecase = GetUserByIdUsecase(self._userRepository)
            await getUserByIDRneUsecase(id)

            await self._userRepository.deleteUser(id)

        except (NoItemsFound, NonExistentUser) as error:
            raise NonExistentUser(error.message)


