"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .jobout import JobOut, JobOutTypedDict
from mistralai.types import BaseModel
import pydantic
from typing import Final, List, Literal, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


JobsOutObject = Literal["list"]


class JobsOutTypedDict(TypedDict):
    total: int
    data: NotRequired[List[JobOutTypedDict]]
    object: NotRequired[JobsOutObject]


class JobsOut(BaseModel):
    total: int

    data: Optional[List[JobOut]] = None

    # fmt: off
    OBJECT: Annotated[Final[Optional[JobsOutObject]], pydantic.Field(alias="object")] = "list" # type: ignore
    # fmt: on
