from datetime import datetime
import pytest

from src.domain.entities.enums import ROLE, YEAR_ENUM, DegreeEnum
from src.domain.entities.user import User
from src.infra.dtos.User.user_dto import CognitoUserDTO


class Test_CognitoUserDTO():

    def test_create_valid_user(self):
        user = User(name='Joao do Teste', ra=19003315, year=YEAR_ENUM._4,
                    course='Engenharia de Computação', email="bruno@bruno.com"
                    )

        userCognitoDto = CognitoUserDTO(user.dict())
        assert userCognitoDto.name == 'Joao Do Teste'
        assert userCognitoDto.ra == '19003315'
        assert userCognitoDto.email == "bruno@bruno.com"
        assert userCognitoDto.course.value == 'Engenharia de Computação'

        userAttributes = userCognitoDto.userAttributes

        expectedAttributes = [
            {'Name': 'custom:name', 'Value': 'Joao Do Teste'},
            {'Name': 'custom:ra', 'Value': '19003315'},
            {'Name': 'custom:email', 'Value': 'bruno@bruno.com'},
            {'Name': 'custom:year', 'Value': 'YEAR_ENUM._4'},
        ]

        for att in expectedAttributes:
            assert att in userAttributes



    def test_parse_valid_user(self):
        user = User(name='Joao do Teste', ra=19003315, year=YEAR_ENUM._3,
                    course=DegreeEnum.ECM, email="bruno@bruno.com"
                    )

        expectedAttributes = [
            {'Name': 'custom:name', 'Value': 'Joao Do Teste'},
            {'Name': 'custom:ra', 'Value': '19003315'},
            {'Name': 'custom:email', 'Value': 'bruno@bruno.com'},
            {'Name': 'custom:year', 'Value': YEAR_ENUM._3},
            {'Name': 'custom:course', 'Value': DegreeEnum.ECM},
        ]


        userCognitoDto = CognitoUserDTO.fromKeyValuePair(expectedAttributes)
        userParsed = userCognitoDto.toEntity()
        assert user == userParsed


