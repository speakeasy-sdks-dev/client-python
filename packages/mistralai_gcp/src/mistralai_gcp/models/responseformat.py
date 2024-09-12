"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from mistralai_gcp.types import BaseModel
from typing import Literal, Optional, TypedDict
from typing_extensions import NotRequired


ResponseFormats = Literal["text", "json_object"]
r"""An object specifying the format that the model must output. Setting to `{ \"type\": \"json_object\" }` enables JSON mode, which guarantees the message the model generates is in JSON. When using JSON mode you MUST also instruct the model to produce JSON yourself with a system or a user message."""


class ResponseFormatTypedDict(TypedDict):
    type: NotRequired[ResponseFormats]


class ResponseFormat(BaseModel):
    type: Optional[ResponseFormats] = "text"
