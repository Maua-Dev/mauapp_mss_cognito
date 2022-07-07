import pytest

from src.domain.entities.enums import ACCESS_LEVEL, ROLE
from src.domain.errors.errors import InvalidCredentials
from src.domain.usecases.login_user_usecase import LoginUserUsecase
from src.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_LoginUserUsecase:

    @pytest.mark.asyncio
    async def test_login_valid_user(self):

        ra = '19003315'
        password = '12345678'

        repository = UserRepositoryMock()

        loginUserUsecase = LoginUserUsecase(repository)
        data = await loginUserUsecase(ra, password)
        expectedAcessToken = 'validAccessToken-' + str(ra)
        expectedRefreshToken = 'validRefreshToken-' + str(ra)

        assert data["accessToken"] == expectedAcessToken
        assert data["refreshToken"] == expectedRefreshToken
        assert data["ra"] == ra
        assert data["name"] == 'Bruno Vilardi'
        assert data["email"] == 'www.link.com.br'


    @pytest.mark.asyncio
    async def test_login_invalid_user(self):
        ra = '87654321'
        password = '12345678'

        repository = UserRepositoryMock()

        loginUserUsecase = LoginUserUsecase(repository)
        with pytest.raises(InvalidCredentials):
            await loginUserUsecase(ra, password)

    @pytest.mark.asyncio
    async def test_login_non_existent_user(self):
        ra = '27550611033'
        password = '123456'

        repository = UserRepositoryMock()

        loginUserUsecase = LoginUserUsecase(repository)
        with pytest.raises(InvalidCredentials):
            await loginUserUsecase(ra, password)
