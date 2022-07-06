import pytest

from src.adapters.controllers.list_users_controller import ListUsersController
from src.adapters.helpers.http_models import HttpRequest
from src.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_ListUsersController:

    @pytest.mark.asyncio
    async def test_list_valid_users(self):
        repository = UserRepositoryMock()

        ra1 = repository._confirmedUsers[0].ra
        ra2 = repository._confirmedUsers[1].ra
        ra3 = 54
        token = "Bearer validAccessToken-19003315"

        req = HttpRequest(body=[ra1, ra2, ra3], headers={'Authorization': token})

        listUsersUsecase = ListUsersController(repository)
        res = await listUsersUsecase(req)


        assert res.status_code == 200
        assert res.body[ra1]["ra"] == repository._confirmedUsers[0].ra
        assert res.body[ra2]["ra"] == repository._confirmedUsers[1].ra
        assert res.body[ra3] == {"error": "User not found"}
