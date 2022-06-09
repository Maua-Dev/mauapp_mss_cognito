from datetime import datetime

import pytest

from src.adapters.controllers.create_user_controller import CreateUserController
from src.adapters.helpers.http_models import HttpRequest
from src.domain.entities.enums import ROLE, ACCESS_LEVEL
from src.infra.repositories.user_repository_mock import UserRepositoryMock


class TestCreateUserController:

    @pytest.mark.asyncio
    async def test_create_valid_user_controller(self):
        request = HttpRequest(body={
            "name": 'user3',
            "ra": '20001236',
            "year": '2002',
            "course": 'Engenharia da Computacao',
            "image": 'www.site.com.br'
        })

        createUserController = CreateUserController(UserRepositoryMock())
        response = await createUserController(request)
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_create_invalid_ra_user_controller(self):
        request = HttpRequest(body={
            "name": 'user3',
            "ra": '1234567890',
            "year": '2002',
            "course": 'Engenharia da Computacao',
            "image": 'www.site.com.br'
        })

        createUserController = CreateUserController(UserRepositoryMock())
        response = await createUserController(request)
        assert response.status_code == 400

    @pytest.mark.asyncio
    async def test_create_invalid_ra2_user_controller(self):
        request = HttpRequest(body={
            "name": 'user3',
            "ra": '22',
            "year": '2002',
            "course": 'Engenharia da Computacao',
            "image": 'www.site.com.br'
        })

        createUserController = CreateUserController(UserRepositoryMock())
        response = await createUserController(request)
        assert response.status_code == 400

    @pytest.mark.asyncio
    async def test_create_invalid_ra3_user_controller(self):
        request = HttpRequest(body={
            "name": 'user3',
            "ra": '-22',
            "year": '2002',
            "course": 'Engenharia da Computacao',
            "image": 'www.site.com.br'
        })

        createUserController = CreateUserController(UserRepositoryMock())
        response = await createUserController(request)
        assert response.status_code == 400

    @pytest.mark.asyncio
    async def test_create_invalid_year_user_controller(self):
        request = HttpRequest(body={
            "name": 'user3',
            "ra": '22',
            "year": '1999',
            "course": 'Engenharia da Computacao',
            "image": 'www.site.com.br'
        })

        createUserController = CreateUserController(UserRepositoryMock())
        response = await createUserController(request)
        assert response.status_code == 400
