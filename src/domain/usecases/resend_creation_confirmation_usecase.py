from src.domain.entities.user import User
from src.domain.errors.errors import EntityError
from src.domain.repositories.user_repository_interface import IUserRepository


class ResendCreationConfirmationUsecase:

    def __init__(self, userRepository: IUserRepository):
        self._userRepository = userRepository

    async def __call__(self, ra: int) -> bool:
        result = await self._userRepository.resendConfirmationCode(ra)
        return result

