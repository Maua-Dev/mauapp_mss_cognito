import pytest

from src.domain.usecases.list_users_usecase import ListUsersUsecase
from src.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_ListUserUsecase:

    @pytest.mark.asyncio
    async def test_list_valid_users(self):
        repository = UserRepositoryMock()

        ra1 = repository._users[0].ra
        ra2 = repository._users[1].ra

        l = [ra1, ra2]
        token = "validAccessToken-19003315"

        listUsersUsecase = ListUsersUsecase(repository)
        userList = await listUsersUsecase(l, token)

        assert len(userList) == 2
        assert userList[ra1] == repository._confirmedUsers[0]
        assert userList[ra2] == repository._confirmedUsers[1]

    @pytest.mark.asyncio
    async def test_list_valid_and_non_exitent_users(self):
        repository = UserRepositoryMock()

        ra1 = repository._users[0].ra
        ra2 = repository._users[1].ra
        ra3 = 57

        l = [ra1, ra2, ra3]
        token = "validAccessToken-19003315"

        listUsersUsecase = ListUsersUsecase(repository)
        userList = await listUsersUsecase(l, token)

        assert len(userList) == 3
        assert userList[ra1] == repository._confirmedUsers[0]
        assert userList[ra2] == repository._confirmedUsers[1]
        assert userList[ra3] == {"error": "User not found"}