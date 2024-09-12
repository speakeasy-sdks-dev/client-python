"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .functioncall import FunctionCall, FunctionCallTypedDict
from mistralai.types import BaseModel, UnrecognizedStr
from mistralai.utils import validate_open_enum
from pydantic.functional_validators import PlainValidator
from typing import Literal, Optional, TypedDict, Union
from typing_extensions import Annotated, NotRequired


ToolTypes = Union[Literal["function"], UnrecognizedStr]


class ToolCallTypedDict(TypedDict):
    function: FunctionCallTypedDict
    id: NotRequired[str]
    type: NotRequired[ToolTypes]


class ToolCall(BaseModel):
    function: FunctionCall

    id: Optional[str] = "null"

    type: Annotated[Optional[ToolTypes], PlainValidator(validate_open_enum(False))] = (
        "function"
    )
