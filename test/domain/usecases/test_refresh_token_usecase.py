import pytest

from src.domain.errors.errors import InvalidToken
from src.domain.usecases.refresh_token_usecase import RefreshTokenUsecase
from src.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_RefreshTokenUsecase:

    @pytest.mark.asyncio
    async def test_refresh_valid_token(self):

        repository = UserRepositoryMock()

        ra = '19003315'
        refreshToken = f'validRefreshToken-{ra}'

        refreshTokenUsecase = RefreshTokenUsecase(repository)
        accessToken, refreshToken = await refreshTokenUsecase(refreshToken)
        expectedAcessToken = 'validAccessToken-' + str(ra)
        expectedRefreshToken = 'validRefreshToken-' + str(ra)

        assert accessToken == expectedAcessToken
        assert refreshToken == expectedRefreshToken

    @pytest.mark.asyncio
    async def test_refresh_token_invalid_token(self):


        ra = '87654321'
        refreshToken = f'invalidRefreshToken-{ra}'

        repository = UserRepositoryMock()

        refreshTokenUsecase = RefreshTokenUsecase(repository)
        with pytest.raises(InvalidToken):
            await refreshTokenUsecase(refreshToken)

    @pytest.mark.asyncio
    async def test_refresh_token_invalid_token2(self):

        ra = '87654321'
        refreshToken = f'validRefreshToken-{ra}'

        repository = UserRepositoryMock()

        refreshTokenUsecase = RefreshTokenUsecase(repository)
        with pytest.raises(InvalidToken):
            await refreshTokenUsecase(refreshToken)
