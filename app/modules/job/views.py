from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from starlette import status

from app.core.db import get_session
from app.models import Job
from app.modules.job.schema import JobRead, Employment, Dismissal


router = APIRouter(prefix='/job')


@router.post('/employment', response_model=JobRead,
             status_code=status.HTTP_200_OK)
def employment(
        data: Employment,
        db: Session = Depends(get_session)
):
    new_employment = Job(**data.dict())

    try:
        db.add(new_employment)
        db.commit()
        db.refresh(new_employment)
    except IntegrityError:
        db.rollback()
        return JobRead(
            error='Employee not exist',
        **new_employment.to_dict()
        )

    return JobRead(
        employee=new_employment.employee.to_dict(),
        **new_employment.to_dict()
    )


@router.put('/dismissal', response_model=JobRead, status_code=status.HTTP_200_OK)
def dismissal(
        id: int,
        data: Dismissal,
        db: Session = Depends(get_session)
):
    job = db.get(Job, id)

    values = data.dict()
    job.update(**values)

    try:
        db.add(job)
        db.commit()
    except IntegrityError:
        db.rollback()

    return job.to_dict()
