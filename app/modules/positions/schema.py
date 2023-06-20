from pydantic import BaseModel


class PositionRead(BaseModel):
    id: int
    title: str
