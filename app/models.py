from sqlalchemy import inspect, Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from app.core.db import Base


class BaseMixin(Base):
    __abstract__ = True

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def update(self, **kwargs) -> None:
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in
                inspect(self).mapper.column_attrs}


class Employee(BaseMixin):
    __tablename__ = "SEA_employees"

    id = Column(Integer, primary_key=True)
    surname = Column(String, nullable=False)
    name = Column(String, nullable=False)
    patronymic = Column(String, nullable=False)
    address = Column(String, nullable=False)
    date_of_birth = Column(String, nullable=False)


class Position(BaseMixin):
    __tablename__ = 'SEA_positions'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)


class Division(BaseMixin):
    __tablename__ = 'SEA_divisions'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)


class Job(BaseMixin):
    __tablename__ = 'SEA_job'

    id = Column(Integer, primary_key=True)
    staffer_id = Column(Integer, ForeignKey('SEA_employees.id'))
    staffer = relationship('Employee')
    position_id = Column(Integer, ForeignKey('SEA_positions.id'))
    position = relationship('Position')
    division_id = Column(Integer, ForeignKey('SEA_divisions.id'))
    division = relationship('Division')
    date_of_employment = Column(String, nullable=False)
    date_of_dismissal = Column(String)
