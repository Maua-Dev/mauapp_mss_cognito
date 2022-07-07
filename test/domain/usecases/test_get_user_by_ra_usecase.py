from datetime import datetime

import pytest

from src.domain.entities.enums import ACCESS_LEVEL, ROLE
from src.domain.entities.user import User
from src.domain.errors.errors import NoItemsFound, NonExistentUser
from src.domain.usecases.get_user_by_ra_usecase import GetUserByRAUsecase
from src.infra.repositories.user_repository_mock import UserRepositoryMock

class Test_GetUserByRAUsecase:

    @pytest.mark.asyncio
    async def test_get_user_by_RA_1(self):
        repo = UserRepositoryMock()
        getUserByRA = GetUserByRAUsecase(repo)
        user = await getUserByRA('19003315')
        assert user == repo._confirmedUsers[0]

    @pytest.mark.asyncio
    async def test_get_user_by_RA_2(self):
        repo = UserRepositoryMock()
        getUserByRA = GetUserByRAUsecase(repo)
        user = await getUserByRA('12345678')
        assert user == repo._confirmedUsers[1]

    @pytest.mark.asyncio
    async def test_get_user_by_non_existent_RA(self):
        getUserByRA = GetUserByRAUsecase(UserRepositoryMock())
        with pytest.raises(NonExistentUser):
            await getUserByRA('87654321')
        with pytest.raises(NonExistentUser):
            await getUserByRA(1248)

