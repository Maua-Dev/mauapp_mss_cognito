import pytest

from src.domain.entities.enums import ACCESS_LEVEL
from src.domain.errors.errors import InvalidToken
from src.domain.usecases.change_password_usecase import ChangePasswordUsecase
from src.domain.usecases.check_token_usecase import CheckTokenUsecase
from src.domain.usecases.confirm_change_password_usecase import ConfirmChangePasswordUsecase
from src.domain.usecases.refresh_token_usecase import RefreshTokenUsecase
from src.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_ConfirmChangePasswordUsecase:

    @pytest.mark.asyncio
    async def test_change_valid_user(self):

        repository = UserRepositoryMock()

        ra = '19003315'
        code = "123456"

        confirmChangePasswordUsecase = ConfirmChangePasswordUsecase(repository)
        result = await confirmChangePasswordUsecase(login=ra, newPassword="teste!!!", code=code)

        assert result
        u = await repository.getUserByRA(ra)
        assert u.password == "teste!!!"

    @pytest.mark.asyncio
    async def test_change_valid_user(self):

        repository = UserRepositoryMock()

        ra = "12345678"
        code = "123456"

        confirmChangePasswordUsecase = ConfirmChangePasswordUsecase(repository)
        result = await confirmChangePasswordUsecase(login=ra, newPassword="teste!!!", code=code)

        assert result
        u = await repository.getUserByRA(ra)
        assert u.password == "teste!!!"


    @pytest.mark.asyncio
    async def test_change_non_existent_user(self):
        repository = UserRepositoryMock()

        ra = "87654321"
        code = "123456"

        confirmChangePasswordUsecase = ConfirmChangePasswordUsecase(repository)
        result = await confirmChangePasswordUsecase(login=ra, newPassword="teste!!!", code=int(code))

        assert not result



    @pytest.mark.asyncio
    async def test_change_invalid_code(self):
        repository = UserRepositoryMock()

        ra = "87654321"
        code = "1234567"

        confirmChangePasswordUsecase = ConfirmChangePasswordUsecase(repository)
        result = await confirmChangePasswordUsecase(login=ra, newPassword="teste!!!", code=code)

        assert not result