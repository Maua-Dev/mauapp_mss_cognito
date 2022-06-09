from src.domain.entities.user import User
from src.domain.errors.errors import UnexpectedError, NoItemsFound, NonExistentUser
from src.domain.repositories.user_repository_interface import IUserRepository


class GetUserByRAUsecase:

    def __init__(self, userRepository: IUserRepository):
        self._userRepository = userRepository

    async def __call__(self, ra: str) -> User:
        try:
            user = await self._userRepository.getUserByRA(RA=ra)

            if user is None:
                raise NonExistentUser('')

            return user

        except (NoItemsFound, NonExistentUser) as error:
            raise NonExistentUser(str(error))



