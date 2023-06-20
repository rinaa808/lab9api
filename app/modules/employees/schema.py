from pydantic import BaseModel


class EmployeeRead(BaseModel):
    id: int
    surname: str
    name: str
    patronymic: str
    address: str
    date_of_birth: str


class EmployeeUpdate(BaseModel):
    surname: str
    name: str
    patronymic: str
    address: str
    date_of_birth: str
