from src.domain.entities.enums import YEAR_ENUM, DegreeEnum


class CheckTokenModel():
    name: str
    ra: str
    year: YEAR_ENUM
    course: DegreeEnum
    valid_token: bool
    email: str
    id = str

    def __init__(self, name: str, ra: str, year: YEAR_ENUM, course: DegreeEnum, valid_token: bool, email: str, id: str = None):
        self.name = name
        self.ra = ra
        self.year = year
        self.course = course
        self.valid_token = valid_token
        self.email = email
        self.id = id

    @staticmethod
    def fromDict(data: dict):
        return CheckTokenModel(
            name=data['name'],
            ra=data['ra'],
            year=data['year'],
            course=data['course'],
            valid_token=data['validToken'],
            email=data['email'],
            id=data['id']
        )

    def toDict(self):
        return {
            'name': self.name,
            'ra': self.ra,
            'year': self.year.value,
            'course': self.course.value,
            'valid_token': self.valid_token,
            'email': self.email,
            'id': self.id if self.id else None
        }
