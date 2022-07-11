from enum import Enum
from typing import List
from wsgiref.validate import validator
import json

from src.domain.entities.enums import ACCESS_LEVEL, ROLE
from src.domain.entities.user import User
from src.infra.dtos.db_base import DbBaseModel


class CognitoUserDTO(DbBaseModel):
    userAttributes: List[dict] = []
    userSub: str
    customAttributes = ['name', 'ra', 'year', 'course', 'email']
    changedFieldNames = {
        'acceptedNotific': 'acceptedNotifications',
        'certWithSocialName': 'certificateWithSocialName'
    }

    def __init__(self, data: dict):
        super().__init__(data)
        self.userSub = data['sub'] if 'sub' in data else None


        defaultDataTemplate = lambda field, value: {
            "Name": field if field not in CognitoUserDTO.customAttributes else f"custom:{field}",
            "Value": value
        }
        for i in self.to_dict():
            if self.__getattribute__(i) is not None and i != 'password' and i != 'userSub':
                self.userAttributes.append(defaultDataTemplate(i, str(self.__getattribute__(i))))


    def toEntity(self):
        return User(
            id=self.id,
            name=self.name,
            ra=self.ra,
            year=self.year,
            course= self.course,
            email=self.email,
        )

    @staticmethod
    def fromKeyValuePair(data: dict):
        dataDict = {}
        for i in data:
            field = i['Name'].removeprefix('custom:')
            try:
                value = i['Value'] if (field != 'accessLevel' and field != 'role') else ACCESS_LEVEL(i['Value']) if field == 'accessLevel' else ROLE(i['Value'])
                fixedField = field if field not in CognitoUserDTO.changedFieldNames else CognitoUserDTO.changedFieldNames[field]
                dataDict[fixedField] = value
            except:
                pass
        return CognitoUserDTO(dataDict)






