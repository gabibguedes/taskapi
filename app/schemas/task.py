from pydantic import BaseModel


class Task(BaseModel):
    title: str
    description: str

    class Config:
        orm_mode = True
