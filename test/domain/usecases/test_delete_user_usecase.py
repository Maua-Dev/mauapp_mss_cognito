import pytest

from src.domain.errors.errors import NonExistentUser
from src.domain.usecases.delete_user_usecase import DeleteUserUsecase
from src.domain.usecases.get_user_by_ra_usecase import GetUserByRAUsecase
from src.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_DeleteUserUsecase:

    @pytest.mark.asyncio
    async def test_delete_valid_user(self):
        repository = UserRepositoryMock()

        ra1 = repository._users[0].ra
        ra2 = repository._users[1].ra

        deleteUserUsecase = DeleteUserUsecase(repository)
        await deleteUserUsecase(ra1)
        await deleteUserUsecase(ra2)

        GetUserByRAUC = GetUserByRAUsecase(repository)
        with pytest.raises(NonExistentUser):
            await GetUserByRAUC(ra1)

        with pytest.raises(NonExistentUser):
            await GetUserByRAUC(ra2)

    @pytest.mark.asyncio
    async def test_delete_non_existent_user(self):
        repository = UserRepositoryMock()
        deleteUserUsecase = DeleteUserUsecase(repository)
        with pytest.raises(NonExistentUser):
            await deleteUserUsecase(12345678915)
        with pytest.raises(NonExistentUser):
            await deleteUserUsecase(15748)