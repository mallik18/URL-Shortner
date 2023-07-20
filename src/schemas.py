""" Modules"""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class UrlRequestData(Basemodel):
    """ Schema for URL Request Data to convert to short URL """
    long-url: str
    tags: list[str]
    expires: datetime
    custom: str | None


class UrlResponseData(Basemodel):
    """ Schema for URL Response Data to respond with converted short URL"""
    long-url: str 
    short-url: str
    created-at: datetime
    active: bool | None
