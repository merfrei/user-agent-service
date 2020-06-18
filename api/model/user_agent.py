"""
User Agent DB and Pydantic Schema
"""

from enum import Enum
from typing import Optional
from pydantic import BaseModel as Schema

from api.model.base import DBModel


class UserAgentDB(DBModel):
    """DB Table Query Manager"""

    tablename = 'user_agents'


class PlatformChoices(str, Enum):
    '''Platform choices/options'''
    persona = 'desktop'
    empresa = 'mobile'


class UserAgentSchema(Schema):
    """Pydantic Schema"""
    string: str
    software: Optional[str] = None
    os: Optional[str] = None
    platform: Optional[PlatformChoices] = None
