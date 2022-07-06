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
            "name": 'user4',
            "ra": '22345678',
            "year": 4,
            "course": 'Engenharia de Computação',
            "email": 'www.site.com.br',
            "password": '22345678'
        })

        createUserController = CreateUserController(UserRepositoryMock())
        response = await createUserController(request)
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_create_invalid_ra_user_controller(self):
        request = HttpRequest(body={
            "name": 'user4',
            "ra": '223456789',
            "year": 4,
            "course": 'Engenharia de Computação',
            "email": 'www.site.com.br',
            "password": '22345678'
        })

        createUserController = CreateUserController(UserRepositoryMock())
        response = await createUserController(request)
        assert response.status_code == 400

    @pytest.mark.asyncio
    async def test_create_invalid_ra2_user_controller(self):
        request = HttpRequest(body={
            "name": 'user4',
            "ra": '22',
            "year": 4,
            "course": 'Engenharia de Computação',
            "email": 'www.site.com.br',
            "password": '22345678'
        })

        createUserController = CreateUserController(UserRepositoryMock())
        response = await createUserController(request)
        assert response.status_code == 400

    @pytest.mark.asyncio
    async def test_create_invalid_ra3_user_controller(self):
        request = HttpRequest(body={
            "name": 'user4',
            "ra": '12345678',
            "year": 4,
            "course": 'Engenharia de Computação',
            "email": 'www.site.com.br',
            "password": '22345678'
        })

        createUserController = CreateUserController(UserRepositoryMock())
        response = await createUserController(request)
        assert response.status_code == 400

    @pytest.mark.asyncio
    async def test_create_invalid_year_user_controller(self):
        request = HttpRequest(body={
            "name": 'user4',
            "ra": '223456789',
            "year": '4',
            "course": 'Engenharia de Computação',
            "email": 'www.site.com.br',
            "password": '22345678'
        })

        createUserController = CreateUserController(UserRepositoryMock())
        response = await createUserController(request)
        assert response.status_code == 400

    @pytest.mark.asyncio
    async def test_create_invalid_year2_user_controller(self):
        request = HttpRequest(body={
            "name": 'user4',
            "ra": '223456789',
            "year": 0,
            "course": 'Engenharia de Computação',
            "email": 'www.site.com.br',
            "password": '22345678'
        })

        createUserController = CreateUserController(UserRepositoryMock())
        response = await createUserController(request)
        assert response.status_code == 400

    @pytest.mark.asyncio
    async def test_create_invalid_year3_user_controller(self):
        request = HttpRequest(body={
            "name": 'user4',
            "ra": '223456789',
            "year": 7,
            "course": 'Engenharia de Computação',
            "email": 'www.site.com.br',
            "password": '22345678'
        })

        createUserController = CreateUserController(UserRepositoryMock())
        response = await createUserController(request)
        assert response.status_code == 400

    @pytest.mark.asyncio
    async def test_create_invalid_year3_user_controller(self):
        request = HttpRequest(body={
            "name": 'user4',
            "ra": '223456789',
            "year": 250250,
            "course": 'Engenharia de Computação',
            "email": 'www.site.com.br',
            "password": '22345678'
        })

        createUserController = CreateUserController(UserRepositoryMock())
        response = await createUserController(request)
        assert response.status_code == 400

    @pytest.mark.asyncio
    async def test_create_invalid_password_user_controller(self):
        request = HttpRequest(body={
            "name": 'user4',
            "ra": '223456789',
            "year": 250250,
            "course": 'Engenharia de Computação',
            "email": 'www.site.com.br',
            "password": '2234'
        })

        createUserController = CreateUserController(UserRepositoryMock())
        response = await createUserController(request)
        assert response.status_code == 400

    @pytest.mark.asyncio
    async def test_create_invalid_password2_user_controller(self):
        request = HttpRequest(body={
            "name": 'user4',
            "ra": '223456789',
            "year": 250250,
            "course": 'Engenharia de Computação',
            "email": 'www.site.com.br'
        })

        createUserController = CreateUserController(UserRepositoryMock())
        response = await createUserController(request)
        assert response.status_code == 400

    @pytest.mark.asyncio
    async def test_create_invalid_password3_user_controller(self):
        request = HttpRequest(body={
            "name": 'user4',
            "ra": '223456789',
            "year": 250250,
            "course": 'Engenharia de Computação',
            "email": 'www.site.com.br',
            "password": ''
        })

        createUserController = CreateUserController(UserRepositoryMock())
        response = await createUserController(request)
        assert response.status_code == 400