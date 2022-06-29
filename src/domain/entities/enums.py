from enum import Enum


class ROLE(Enum):
    ADMIN = "ADMIN"
    STUDENT = "STUDENT"
    PROFESSOR = "PROFESSOR"
    SPEAKER = "SPEAKER"

    def __str__(self):
        return self.value


class ACCESS_LEVEL(Enum):
    ADMIN = "ADMIN"
    USER = "USER"
    SPEAKER = "SPEAKER"

    def __str__(self):
        return self.value


class YEAR_ENUM(Enum):
    _1 = 1
    _2 = 2
    _3 = 3
    _4 = 4
    _5 = 5
    _6 = 6



class DegreeEnum(Enum):
    ADM = "Administração"
    DSG = "Design"
    EFB = "Engenharia Fundamentos Básicos"
    EFH = "Engenharia Fundamentos Humanos"
    EAD = "Ensino a Distância"
    ETE = "Engenharia Tronco Eletrica"
    ETM = "Engenharia Tronco Mecânica"
    ETQ = "Engenharia Tronco Química"
    TTI = "Tronco Tecnologias da Informação"
    EAL = "Engenharia de Alimentos"
    ETC = "Engenharia Civíl"
    EMC = "Engenharia Mecânica"
    EQM = "Engenharia Química"
    EPM = "Engenharia de Produção"
    ECA = "Engenharia de Controle e Automação"
    EET = "Engenharia Elétrica"
    EEN = "Engenharia Eletrônica"
    EEE = "Engenharia Elétrica e Eletrônica"
    ECM = "Engenharia de Computação"


