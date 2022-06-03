from abc import ABC, abstractmethod
from typing import List

from src.infra.dtos.User.user_dto import CognitoUserDTO


class IDataSource(ABC):
    @abstractmethod
    def getAllUsers(self, userId: int) -> List[CognitoUserDTO]:
        pass

    @abstractmethod
    def getUserById(self,codeSubject: str) -> CognitoUserDTO:
        pass