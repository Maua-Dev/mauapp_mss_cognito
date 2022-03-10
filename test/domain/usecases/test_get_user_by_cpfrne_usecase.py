from datetime import datetime

import pytest

from src.domain.entities.enums import ACCESS_LEVEL, ROLE
from src.domain.entities.user import User
from src.domain.errors.errors import NoItemsFound, NonExistentUser
from src.domain.usecases.get_user_by_cpfrne_usecase import GetUserByCpfRneUsecase
from src.infra.repositories.user_repository_mock import UserRepositoryMock

class Test_GetUserByCpfRneUsecase:

    @pytest.mark.asyncio
    async def test_get_user_by_cpfrne_1(self):
        getUserByCpfRne = GetUserByCpfRneUsecase(UserRepositoryMock())
        user = await getUserByCpfRne(12345678910)
        assert user == User(name='user1', cpfRne=12345678910, ra=19003315, role=ROLE.STUDENT,
                 accessLevel=ACCESS_LEVEL.USER, createdAt=datetime(2022, 3, 8, 22, 10),
                 updatedAt=datetime(2022, 3, 8, 22, 15), email='bruno@bruno.com'
                        )

    @pytest.mark.asyncio
    async def test_get_user_by_cpfrne_2(self):
        getUserByCpfRne = GetUserByCpfRneUsecase(UserRepositoryMock())
        user = await getUserByCpfRne(12345678911)
        assert user == User(name='user2', cpfRne=12345678911, ra=20001231, role=ROLE.PROFESSOR,
                 accessLevel=ACCESS_LEVEL.ADMIN, createdAt=datetime(2022, 2, 15, 23, 15),
                 updatedAt=datetime(2022, 2, 15, 23, 15)
                        )

    @pytest.mark.asyncio
    async def test_get_user_by_non_existent_cpfrne(self):
        getUserByCpfRne = GetUserByCpfRneUsecase(UserRepositoryMock())
        with pytest.raises(NonExistentUser):
            await getUserByCpfRne(12345678912)
        with pytest.raises(NonExistentUser):
            await getUserByCpfRne(1248)

