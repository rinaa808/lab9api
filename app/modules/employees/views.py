from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from starlette import status

from app.core.db import get_session
from app.models import Employee
from app.modules.employees.schema import EmployeeRead, EmployeeUpdate

router = APIRouter(prefix='/employee')


@router.post('/create', status_code=status.HTTP_200_OK)
def create_employee(
        surname: str,
        name: str,
        patronymic: str,
        address: str,
        date_of_birth: str,
        db: Session = Depends(get_session)
):
    employee = Employee(
        surname=surname,
        name=name,
        patronymic=patronymic,
        address=address,
        date_of_birth=date_of_birth)

    try:
        db.add(employee)
        db.commit()
    except IntegrityError:
        db.rollback()
        return status.HTTP_500_INTERNAL_SERVER_ERROR

    return employee.to_dict()


@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_employee(
        id: int,
        db: Session = Depends(get_session)
):
    employee = db.get(Employee, id)

    if not employee:
        return status.HTTP_404_NOT_FOUND
    return employee.to_dict()


@router.get('/all', status_code=status.HTTP_200_OK)
def get_employees(
        name: str = None,
        db: Session = Depends(get_session)
):
    query = select(Employee)

    if name:
        query = query.where(Employee.name == name)

    employees = db.scalars(query).all()

    return [employee.to_dict() for employee in employees]


@router.put('/update', response_model=EmployeeRead, status_code=status.HTTP_200_OK)
def update_employee(
        id: int,
        data: EmployeeUpdate,
        db: Session = Depends(get_session)
):
    employee = db.get(Employee, id)

    values = data.dict()
    employee.update(**values)

    try:
        db.add(employee)
        db.commit()
    except IntegrityError:
        db.rollback()

    return employee.to_dict()


@router.put('/delete', response_model=EmployeeRead, status_code=status.HTTP_200_OK)
def delete_employee(
        id: int,
        db: Session = Depends(get_session)
):
    employee = db.get(Employee, id)

    try:
        db.delete(employee)
        db.commit()
    except IntegrityError:
        db.rollback()
    return 'deletion successful'
