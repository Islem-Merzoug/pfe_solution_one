from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.database import (
    add_file,
    delete_file,
    retrieve_file,
    retrieve_files,
    update_file,
)
from app.model.file import (
    ErrorResponseModel,
    ResponseModel,
    FileSchema,
    UpdateFileModel,
)

router = APIRouter()