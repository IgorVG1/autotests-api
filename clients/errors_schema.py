from pydantic import BaseModel, Field, ConfigDict
from typing import Any, Dict, List


class ValidationErrorSchema(BaseModel):
    """
    Модель, описывающая структуру ошибки валидации API.
    Attributes:
        type: str
        location: List[str] (loc)
        message: str (msg)
        input: Any
        context: Dict[str, Any] (ctx)
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    type: str
    location: List[str] = Field(alias="loc")
    message: str = Field(alias="msg")
    input: Any
    context: Dict[str, Any] = Field(alias="ctx")


class ValidationErrorResponseSchema(BaseModel):
    """
    Модель, описывающая структуру ответа API с ошибкой валидации.
    Attributes:
        details: List[ValidationErrorSchema] (detail)
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
    details: List[ValidationErrorSchema] = Field(alias="detail")


class InternalErrorResponseSchema(BaseModel):
    """
    Модель для описания внутренней ошибки.
    Attributes:
        detail: str
    """
    detail: str