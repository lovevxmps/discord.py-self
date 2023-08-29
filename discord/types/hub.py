"""
The MIT License (MIT)

Copyright (c) 2021-present Dolfies

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from typing import Dict, List, Literal, Optional, TypedDict, Union
from typing_extensions import NotRequired

from .guild import Guild
from .snowflake import Snowflake


class HubWaitlist(TypedDict):
    email: str
    email_domain: str
    school: str
    user_id: Snowflake


class HubGuild(TypedDict):
    id: Snowflake
    name: str
    icon: Optional[str]


class EmailDomainLookup(TypedDict):
    guilds_info: NotRequired[List[HubGuild]]
    has_matching_guild: bool


class EmailDomainVerification(TypedDict):
    guild: Guild
    joined: bool
