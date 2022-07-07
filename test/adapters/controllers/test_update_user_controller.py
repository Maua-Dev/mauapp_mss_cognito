from datetime import datetime

import pytest

from src.adapters.controllers.update_user_controller import UpdateUserController
from src.adapters.helpers.http_models import HttpRequest
from src.domain.entities.enums import ROLE, ACCESS_LEVEL
from src.infra.repositories.user_repository_mock import UserRepositoryMock


class TestUpdateUserController:


    @pytest.mark.asyncio
    async def test_update_valid_user_controller(self):
        req = {
            "name": 'Bruno Vilardi',
        }
        header = {"Authorization": "Bearer validAccessToken-19003315"}
        request = HttpRequest(body=req, headers=header)

        updateUserController = UpdateUserController(UserRepositoryMock())
        response = await updateUserController(request)
        assert response.status_code == 200


    @pytest.mark.asyncio
    async def test_update_invalid_user_controller(self):
        req = {
            "name": 'Johny White',
        }
        header = {"Authorization": "Bearer validAccessToken-87654321"}
        request = HttpRequest(body=req, headers=header)

        updateUserController = UpdateUserController(UserRepositoryMock())
        response = await updateUserController(request)
        assert response.status_code == 400



