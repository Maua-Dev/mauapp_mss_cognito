from datetime import datetime

import pytest

from src.domain.entities.enums import ACCESS_LEVEL, ROLE
from src.domain.entities.user import User
from src.domain.errors.errors import NonExistentUser, EntityError
from src.domain.usecases.confirm_user_creation_usecase import ConfirmUserCreationUsecase
from src.domain.usecases.create_user_usecase import CreateUserUsecase
from src.domain.usecases.get_user_by_ra_usecase import GetUserByRAUsecase
from src.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_CreateUserUsecase:

    @pytest.mark.asyncio
    async def test_create_valid_user(self):
        newUser = User(name='Joana da Testa', ra=20004239, year=2022,
                 course="Engenharia de teste", image="www.link.com.br",
                )

        repository = UserRepositoryMock()

        # confirm user does not exist yet
        GetUserByRA = GetUserByRAUsecase(repository)
        with pytest.raises(NonExistentUser):
            await GetUserByRA('20004239')


        # create user
        createUserUsecase = CreateUserUsecase(repository)
        await createUserUsecase(newUser)

        # confirm user
        confirmUserUseCase = ConfirmUserCreationUsecase(repository)
        await confirmUserUseCase('20004239', '1234567')

        # confirm user exists
        GetUserByRA = GetUserByRAUsecase(repository)
        createdUser = await GetUserByRA('20004239')
        assert createdUser is not None

        assert createdUser.name == 'Joana Da Testa'
        assert createdUser.ra == '20004239'

    @pytest.mark.asyncio
    async def test_create_invalid_user(self):
        with pytest.raises(EntityError):
            newUser = User(name='Joana da Testa', ra=20004239, year=-1997,
                     course="Engenharia de teste", image="www.link.com.br",
                    )
            repository = UserRepositoryMock()
            createUserUsecase = CreateUserUsecase(repository)