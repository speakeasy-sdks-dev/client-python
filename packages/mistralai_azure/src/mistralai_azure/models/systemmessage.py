"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .contentchunk import ContentChunk, ContentChunkTypedDict
from mistralai_azure.types import BaseModel
from typing import List, Literal, Optional, TypedDict, Union
from typing_extensions import NotRequired


ContentTypedDict = Union[str, List[ContentChunkTypedDict]]


Content = Union[str, List[ContentChunk]]


Role = Literal["system"]


class SystemMessageTypedDict(TypedDict):
    content: ContentTypedDict
    role: NotRequired[Role]


class SystemMessage(BaseModel):
    content: Content

    role: Optional[Role] = "system"
