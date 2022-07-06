import pytest

from src.adapters.controllers.resend_creation_confirmation_controller import ResendCreationConfirmationController
from src.adapters.helpers.http_models import HttpRequest
from src.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_ResendCreationConfirmationController:

    @pytest.mark.asyncio
    async def test_resend_valid_ra(self):
        request = HttpRequest(body={
            'ra': '19003315'
        })

        repository = UserRepositoryMock()
        resendCreationConfirmationController = ResendCreationConfirmationController(repository)
        response = await resendCreationConfirmationController(request)
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_resend_invalid_ra(self):
        request = HttpRequest(body={
            'cpf_rne': '87654321'
        })

        repository = UserRepositoryMock()
        resendCreationConfirmationController = ResendCreationConfirmationController(repository)
        response = await resendCreationConfirmationController(request)
        assert response.status_code == 400
