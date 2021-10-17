from typing import Optional, List

from pydantic import BaseModel, EmailStr, Field
from datetime import datetime, time, timedelta, date


class FileSchema(BaseModel):
    name: str = Field(...)
    date: datetime = Field(...)
    type : str = Field(...)
    service : int = Field(...)
    choice: Optional[str] = Field(...)
    inputLink: str = Field(...)
    outputLink: str = Field(...)
    user_id: str = Field(...)


    class Config:
        schema_extra = {
            "example": {
                "name": "islem",
                "date": "2008-09-15T15:53:00+05:00",
                "type": 'jpg',
                "service": 1,
                "choice": 'detect_gender',
                "inputLink": "inputLink",
                "outputLink": "outputLink",
                "user_id": "user_id"
            }
        }


class UpdateFileModel(BaseModel):
    name: Optional[str] = Field(...)
    date: Optional[datetime] = Field(...)
    type : Optional[str] = Field(...)
    service : Optional[int] = Field(...)
    inputLink: Optional[str] = Field(...)
    outputLink: Optional[str] = Field(...)
    user_id: Optional[str] = Field(...)


    class Config:
        schema_extra = {
            "example": {
                "name": "islem",
                "date": "2008-09-15T15:53:00+05:00",
                "type": 'jpg',
                "service": 1,
                "inputLink": "inputLink",
                "outputLink": "outputLink",
                "user_id": "user_id"
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}