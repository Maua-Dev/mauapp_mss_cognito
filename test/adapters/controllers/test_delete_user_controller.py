import pytest

from src.adapters.controllers.delete_user_controller import DeleteUserController
from src.adapters.helpers.http_models import HttpRequest
from src.domain.errors.errors import NonExistentUser
from src.domain.usecases.get_user_by_ra_usecase import GetUserByRAUsecase
from src.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_DeleteUserUsecase:

    @pytest.mark.asyncio
    async def test_delete_valid_user(self):
        repository = UserRepositoryMock()

        req1 = HttpRequest(body={"login": repository._users[0].ra, "id": repository._users[0].id})
        req2 = HttpRequest(body={"login": repository._users[1].ra, "id": repository._users[1].id})

        deleteUserController = DeleteUserController(repository)
        res1 = await deleteUserController(req1)
        res2 = await deleteUserController(req2)

        assert res1.status_code == 200
        assert res2.status_code == 200


    @pytest.mark.asyncio
    async def test_delete_non_existent_user(self):
        repository = UserRepositoryMock()

        req1 = HttpRequest(body={"login": repository._users[0].ra, "id": repository._users[0].id})

        deleteUserController = DeleteUserController(repository)
        res1 = await deleteUserController(req1)
        res2 = await deleteUserController(req1)

        assert res1.status_code == 200
        assert res2.status_code == 400

    @pytest.mark.asyncio
    async def test_delete_user_with_invalid_cpf_rne(self):
        repository = UserRepositoryMock()

        req1 = HttpRequest(body={"login": repository._users[2].ra, "id": repository._users[2].id})
        deleteUserController = DeleteUserController(repository)
        res1 = await deleteUserController(req1)
        assert res1.status_code == 400

