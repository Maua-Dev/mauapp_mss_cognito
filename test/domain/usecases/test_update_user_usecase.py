from datetime import datetime

import pytest

from src.domain.entities.enums import YEAR_ENUM, DegreeEnum
from src.domain.entities.user import User
from src.domain.errors.errors import InvalidToken
from src.domain.usecases.get_user_by_ra_usecase import GetUserByRAUsecase
from src.domain.usecases.update_user_usecase import UpdateUserUsecase
from src.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_UpdateUserUsecase:

    @pytest.mark.asyncio
    async def test_update_existent_user(self):
        oldUser = User(id="123", name='Bruno Vilardi', ra=19003315, year=YEAR_ENUM._4,
                 course='Engenharia de Computação', email="www.link.com.br", password='12345678'
                 )

        newUser = oldUser.copy()
        newUser.name = 'user1_'

        repository = UserRepositoryMock()

        updateUserUsecase = UpdateUserUsecase(repository)
        await updateUserUsecase(newUser.dict(), f"validAccessToken-{oldUser.ra}")

        # confirm user was updated
        getUserByRAUsecase = GetUserByRAUsecase(repository)
        updatedUser = await getUserByRAUsecase(newUser.ra)

        assert updatedUser is not None
        assert updatedUser.name == 'user1_'
        assert updatedUser.name != oldUser.name
        assert updatedUser.ra == oldUser.ra
        assert updatedUser.email == oldUser.email

    @pytest.mark.asyncio
    async def test_update_existent_user2(self):
        oldUser = User(id="345", name='Hector Ronaldo', ra=12345678, year=YEAR_ENUM._3,
                 course='Engenharia de Computação', email="user2@user.com"
                 )

        newUser = oldUser.copy()
        newUser.name = 'user2_'

        repository = UserRepositoryMock()

        updateUserUsecase = UpdateUserUsecase(repository)
        await updateUserUsecase(newUser.dict(), f"validAccessToken-{oldUser.ra}")

        # confirm user was updated
        getUserByRAUsecase = GetUserByRAUsecase(repository)
        updatedUser = await getUserByRAUsecase(newUser.ra)

        assert updatedUser is not None
        assert updatedUser.name == 'user2_'
        assert updatedUser.name != oldUser.name
        assert updatedUser.ra == oldUser.ra
        assert updatedUser.email == oldUser.email

    @pytest.mark.asyncio
    async def test_update_non_existent_user(self):
        newUser = User(id="678", name='Johny White', ra=87654321, year=YEAR_ENUM._5,
                 course='Engenharia de Computação', email="www.link.com.br", password='12345678'
                 )
        repository = UserRepositoryMock()
        updateUserUsecase = UpdateUserUsecase(repository)

        with pytest.raises(InvalidToken):
            await updateUserUsecase(newUser.dict(), f"validAccessToken-{newUser.ra}")