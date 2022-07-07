from datetime import datetime

import pytest
from pydantic import ValidationError

from src.domain.entities.enums import YEAR_ENUM, DegreeEnum
from src.domain.entities.user import User
from src.domain.errors.errors import EntityError


class Test_User():

    def test_create_valid_user(self):
        user = User(id="123", name='Bruno Vilardi', ra=19003315, year=YEAR_ENUM._4,
                 course=DegreeEnum.ECM, email="bruno@bruno.com"
                )

        assert user.name == 'Bruno Vilardi'
        assert user.ra == '19003315'
        assert user.year == YEAR_ENUM._4
        assert user.course.value == 'Engenharia de Computação'
        assert user.email == 'bruno@bruno.com'

    def test_create_valid_user1(self):
        user = User(name='Joao do Teste', ra='12345678',
                    year=YEAR_ENUM._1, course='Engenharia Fundamentos Básicos',
                    email='www.google.com'
                    )

        assert len(user.name) > 0
        assert user.name == 'Joao Do Teste'
        assert len(user.ra) == 8
        assert user.ra == '12345678'
        assert user.year.value == 1
        assert len(user.course.value) > 0
        assert user.course.value == 'Engenharia Fundamentos Básicos'
        assert user.email == 'www.google.com'

    def test_create_valid_user2(self):
        user = User(name='Joao do Teste', ra='87654321',
                    year=YEAR_ENUM._6, course='Ensino a Distância',
                    email='www.google.com', password="12345679"
                    )

        assert len(user.name) > 0
        assert user.name == 'Joao Do Teste'
        assert user.ra == '87654321'
        assert user.year == YEAR_ENUM._6
        assert user.year.value > 0
        assert len(user.course.value) > 0
        assert user.course == DegreeEnum.EAD
        assert user.email == 'www.google.com'
        assert user.password == '12345679'
        assert len(user.password) >= 8


    def test_create_invalid_user1(self):
        with pytest.raises((EntityError, ValidationError)):
            User(ra='87654321',
                 year=YEAR_ENUM._6, course='Ensino a Distância',
                 email='www.google.com', password="12345679"
                 )

    def test_create_invalid_user2(self):
        with pytest.raises((EntityError, ValidationError)):
            User(name='Joao do Teste', ra='87654321',
                 year=2002, course='Ensino a Distância',
                 email='www.google.com', password="12345679"
                 )

    def test_create_invalid_user3(self):
        with pytest.raises((EntityError, ValidationError)):
            User(name='Joao do Teste', ra='87654321',
                 year=YEAR_ENUM._3, course='Ensino a Distância',
                 )

    def test_create_invalid_user4(self):
        with pytest.raises((EntityError, ValidationError)):
            User(name='Joao do Teste', ra='123456789101112',
                 year=YEAR_ENUM._6, course='Ensino a Distância',
                 email='www.google.com', password="12345679"
                 )

    def test_create_invalid_user5(self):
        with pytest.raises((EntityError, ValidationError)):
            User(name='Joao do Teste',
                 year=YEAR_ENUM._6, course='Ensino a Distância',
                 email='www.google.com', password="12345679"
                 )

    def test_create_invalid_user6(self):
        with pytest.raises((EntityError, ValidationError)):
            User(name='Joao do Teste', ra='87654321',
                 year=1984, course='Ensino a Distância',
                 email='www.google.com', password="12345679"
                 )

    def test_create_invalid_user7(self):
        with pytest.raises((EntityError, ValidationError)):
            User(name='Joao do Teste', ra='123456789',
                 year=YEAR_ENUM._3.value, course='Ensino a Distância',
                 image='www.google.com'
                 )

    def test_create_invalid_user8(self):
        with pytest.raises((EntityError, ValidationError)):
            User(name='Joao do Teste', ra='123456789',
                 year=YEAR_ENUM._3.value, course=DegreeEnum.ECM,
                 image='www.google.com'
                 )

    def test_create_invalid_user9(self):
        with pytest.raises((EntityError, ValidationError)):
            User(name='Joao do Teste', ra='123456789',
                 year=YEAR_ENUM._3.value, image='www.google.com'
                 )