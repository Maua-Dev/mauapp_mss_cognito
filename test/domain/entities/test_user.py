from datetime import datetime

import pytest
from pydantic import ValidationError

from src.domain.entities.user import User
from src.domain.errors.errors import EntityError


class Test_User():

    def test_create_valid_user(self):
        user = User(name='Joao do Teste', ra='19003315',
                    year=2022, course='Engenharia de algo',
                    image='www.google.com'
                )

        assert len(user.name) > 0
        assert user.name == 'Joao Do Teste'
        assert user.ra == '19003315'
        assert user.year == 2022
        assert user.year > 0
        assert len(user.course) > 0
        assert user.course == 'Engenharia de algo'
        assert user.image == 'www.google.com'

    def test_create_valid_user1(self):
        user = User(name='Joao do Teste', ra='12345678',
                    year=2000, course='Engenharia de algo',
                    image='www.google.com'
                    )

        assert len(user.name) > 0
        assert user.name == 'Joao Do Teste'
        assert len(user.ra) == 8
        assert user.ra == '12345678'
        assert user.year == 2000
        assert user.year > 0
        assert len(user.course) > 0
        assert user.course == 'Engenharia de algo'
        assert user.image == 'www.google.com'

    def test_create_valid_user2(self):
        user = User(name='joao do teste', ra='12345678',
                    year=2000, course='Engenharia de algo',
                    image='www.google.com'
                )

        assert len(user.name) > 0
        assert user.name == 'Joao Do Teste'
        assert user.ra == '12345678'
        assert user.year == 2000
        assert user.year > 0
        assert len(user.course) > 0
        assert user.course == 'Engenharia de algo'
        assert user.image == 'www.google.com'


    def test_create_invalid_user1(self):
        with pytest.raises(EntityError):
            User(name='', ra='12345678',
                    year=2000, course='Engenharia de algo',
                    image='www.google.com'
                 )

    def test_create_invalid_user2(self):
        with pytest.raises(EntityError):
            User(name='Joao do Teste', ra='1234567',
                    year=2000, course='Engenharia de algo',
                    image='www.google.com'
                 )

    def test_create_invalid_user3(self):
        with pytest.raises(EntityError):
            User(name='Joao do Teste', ra='12345678',
                    year=1999, course='Engenharia de algo',
                    image='www.google.com'
                 )

    def test_create_invalid_user4(self):
        with pytest.raises(EntityError):
            User(name='Joao do Teste', ra='12345678',
                    year=2000, course='',
                    image='www.google.com'
                 )

    def test_create_invalid_user5(self):
        with pytest.raises((EntityError, ValidationError)):
            User(name='Joao do Teste', ra='12345678',
                    year=2000, course='Engenharia de algo',
                    image=''
                 )

    def test_create_invalid_user6(self):
        with pytest.raises((EntityError, ValidationError)):
            User(name='Joao do Teste', ra='12345678',
                    year=-1922, course='Engenharia de algo',
                    image='www.google.com'
                 )

    def test_create_invalid_user7(self):
        with pytest.raises((EntityError, ValidationError)):
            User(name='Joao do Teste', ra='123456789',
                 year=2000, course='Engenharia de algo',
                 image='www.google.com'
                 )

    def test_create_invalid_user8(self):
        with pytest.raises((EntityError, ValidationError)):
            User(name='Joao do Teste', ra='',
                    year=2000, course='Engenharia de algo',
                    image='www.google.com'
                    )