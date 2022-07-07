import pytest

from src.domain.errors.errors import NonExistentUser, EntityError
from src.domain.usecases.resend_creation_confirmation_usecase import ResendCreationConfirmationUsecase
from src.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_ResendUserCreationConfirmationUsecase:

    @pytest.mark.asyncio
    async def test_resend_valid_user(self):

        repository = UserRepositoryMock()

        ra = '19003315'

        resendUserCreationConfirmationUsecase = ResendCreationConfirmationUsecase(repository)
        result = await resendUserCreationConfirmationUsecase(ra)

        assert result

    @pytest.mark.asyncio
    async def test_resend_invalid_ra(self):

        repository = UserRepositoryMock()

        ra = '43289456021'

        resendUserCreationConfirmationUsecase = ResendCreationConfirmationUsecase(repository)

        with pytest.raises(NonExistentUser):
            await resendUserCreationConfirmationUsecase(ra)

    @pytest.mark.asyncio
    async def test_resend_nonexistent_user(self):

        repository = UserRepositoryMock()

        ra = '87654321'

        resendUserCreationConfirmationUsecase = ResendCreationConfirmationUsecase(repository)

        with pytest.raises(NonExistentUser):
            await resendUserCreationConfirmationUsecase(ra)
