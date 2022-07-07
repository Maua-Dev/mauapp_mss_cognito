import pytest

from src.domain.entities.enums import ACCESS_LEVEL
from src.domain.errors.errors import InvalidToken
from src.domain.usecases.check_token_usecase import CheckTokenUsecase
from src.domain.usecases.refresh_token_usecase import RefreshTokenUsecase
from src.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_CheckTokenUsecase:

    @pytest.mark.asyncio
    async def test_check_valid_token(self):

        repository = UserRepositoryMock()

        ra = '19003315'
        accessToken = f'validAccessToken-{ra}'

        checkTokenUsecase = CheckTokenUsecase(repository)
        data = await checkTokenUsecase(accessToken)

        assert data['ra'] == ra
        assert data['name'] == 'Bruno Vilardi'
        assert data['email'] == 'www.link.com.br'

    @pytest.mark.asyncio
    async def test_check_token_invalid_token(self):


        ra = '87654321'
        refreshToken = f'invalidAccessToken-{ra}'

        repository = UserRepositoryMock()

        checkTokenUsecase = CheckTokenUsecase(repository)
        with pytest.raises(InvalidToken):
            await checkTokenUsecase(refreshToken)

    @pytest.mark.asyncio
    async def test_check_invalid_token2(self):

        ra = '87654321'
        refreshToken = f'validAccessToken-{ra}'

        repository = UserRepositoryMock()

        checkTokenUsecase = CheckTokenUsecase(repository)
        with pytest.raises(InvalidToken):
            await checkTokenUsecase(refreshToken)