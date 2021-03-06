import pytest

from src.adapters.controllers.change_password_controller import ChangePasswordController
from src.adapters.controllers.confirm_change_password_controller import ConfirmChangePasswordController
from src.adapters.controllers.login_user_controller import LoginUserController
from src.adapters.controllers.update_user_controller import UpdateUserController
from src.adapters.helpers.http_models import HttpRequest
from src.domain.entities.enums import ROLE, ACCESS_LEVEL
from src.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_ChangePasswordController:

    @pytest.mark.asyncio
    async def test_change_valid_cpfRne_controller(self):
        request = HttpRequest(body={
            'login': '75599469093',
            'new_password': 'teste!!!123',
            'confirmation_code': '123456'
        })

        repository = UserRepositoryMock()
        confirmChangePasswordController = ConfirmChangePasswordController(repository)
        response = await confirmChangePasswordController(request)
        assert response.status_code == 200
        assert response.body == {
            'result': True,
            'message': ''
        }
        u = await repository.getUserByRA('75599469093')
        assert u.password == 'teste!!!123'

    @pytest.mark.asyncio
    async def test_change_valid_email_controller(self):
        request = HttpRequest(body={
            'login': "user2@user.com",
            'new_password': 'teste!!!123',
            'confirmation_code': '123456'
        })

        repository = UserRepositoryMock()
        confirmChangePasswordController = ConfirmChangePasswordController(repository)
        response = await confirmChangePasswordController(request)
        assert response.status_code == 200
        assert response.body == {
            'result': True,
            'message': ''
        }
        u = await repository.getUserByRA('64968222041')
        assert u.password == 'teste!!!123'

    @pytest.mark.asyncio
    async def test_change_non_existent_cpfRne_controller(self):
        request = HttpRequest(body={
            'login': 15418,
            'new_password': 'teste!!!123',
            'confirmation_code': '123456'
        })

        repository = UserRepositoryMock()
        confirmChangePasswordController = ConfirmChangePasswordController(repository)
        response = await confirmChangePasswordController(request)
        assert response.status_code == 400
        assert response.body == {
            'result': False,
            'message': 'User not found, invalid confirmation code or weak new password.'
        }







