from src.domain.entities.enums import ROLE, YEAR_ENUM


class LoginUserModel():
    accessToken: str
    refreshToken: str
    id: str
    year: YEAR_ENUM
    ra: int
    email: str
    name: str

    def __init__(self, accessToken: str, refreshToken: str, year: int, ra: int, email: str,name: str, id: str=None):
        self.accessToken = accessToken
        self.refreshToken = refreshToken
        self.id = id
        self.year = year
        self.ra = ra
        self.email = email
        self.name = name

    @staticmethod
    def fromDict(data: dict):
        return LoginUserModel(
        accessToken = data['accessToken'],
        refreshToken = data['refreshToken'],
        id = data['id'],
        year = data['year'],
        ra=data['ra'],
        email=data['email'],
        name=data['name'],
        )

    def toDict(self):
        return {
            'access_token': self.accessToken,
            'refresh_token': self.refreshToken,
            'id': self.id,
            'year': self.year.value,
            'ra': self.ra,
            'email': self.email,
            'name': self.name,
        }
