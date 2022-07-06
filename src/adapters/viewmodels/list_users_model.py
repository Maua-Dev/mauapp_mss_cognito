from src.domain.entities.enums import ROLE, ACCESS_LEVEL


class ListUserError():
    def __init__(self, message):
        self.message = message

    def toDict(self):
        return self.message


class ListUserModel():
    role: ROLE
    accessLevel: ACCESS_LEVEL
    ra: int
    email: str
    name: str

    def __init__(self, role: ROLE, accessLevel: ACCESS_LEVEL, ra: int, email: str, name: str):
        self.role = role
        self.accessLevel = accessLevel
        self.ra = ra
        self.email = email
        self.name = name

    def fromDict(dict):
        if "error" in dict:
            return ListUserError(dict)
        return ListUserModel(
            role=dict.get('role').value if dict.get('role') else None,
            accessLevel=dict.get('accessLevel').value if dict.get('accessLevel') else None,
            ra=dict.get('ra') if dict.get('ra') else None,
            email=dict.get('email') if dict.get('email') else None,
            name=dict.get('name') if dict.get('name') else None,
        )

    def toDict(self):
        return {
            'role': self.role,
            'accessLevel': self.accessLevel,
            'ra': self.ra,
            'email': self.email,
            'name': self.name,
        }

class ListUsersModel():
    users: dict

    def __init__(self, usersDict: dict):
        self.users = {}
        for userId in usersDict.keys():
            userModel = ListUserModel.fromDict(usersDict[userId])
            self.users[userId] = userModel.toDict()

    def toDict(self):
        return self.users



