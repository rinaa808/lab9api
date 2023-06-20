from pydantic import BaseModel

from app.modules.employees.schema import EmployeeRead
from app.modules.positions.schema import PositionRead
from app.modules.divisions.schema import DivisionRead


class JobRead(BaseModel):
    id: int = None
    staffer: EmployeeRead = None
    position: PositionRead = None
    division: DivisionRead = None
    date_of_employment: str
    date_of_dismissal: str


class Employment(BaseModel):
    staffer_id: int
    position_id: int
    division_id: int
    date_of_employment: str
    date_of_dismissal: str


class Dismissal(BaseModel):
    id: int = None
    staffer: EmployeeRead = None
    position: PositionRead = None
    division: DivisionRead = None
    date_of_employment: str
    date_of_dismissal: str
