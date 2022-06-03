from src.domain.entities.user import User
from src.domain.errors.errors import UserAlreadyExists, UnexpectedError, IncompleteUser, InvalidCredentials
from src.domain.repositories.user_repository_interface import IUserRepository


class LoginUserUsecase:

    def __init__(self, userRepository: IUserRepository):
        self._userRepository = userRepository

    async def __call__(self, ra: int, password: str) -> dict:
        loginResponseFields = ['name', 'ra', 'year', 'course', 'image']
        data = await self._userRepository.loginUser(ra, password)
        if data is None:
            raise InvalidCredentials(f'Ra and password don`t match')
        if not set(loginResponseFields) <= set(data.keys()):
            raise UnexpectedError(f'Unexpected response from repository - missing fields from {loginResponseFields}')
        return data
