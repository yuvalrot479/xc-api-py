from .....types import RecordingMethod
from .....tags.meta import SinceTag
from ....constants import aliases
from ..serializers import serialize_boolean, serialize_datetime_date

from typing import Annotated, Union, Optional
from pydantic import Field, PlainSerializer
import datetime


PlaybackField = Annotated[
  Optional[bool],
  Field(
    default=None,
    title='Playback was used to lure the animal.',
    serialization_alias=aliases.PLAYBACK_USED,
  ),
  PlainSerializer(serialize_boolean),
]

AutomaticField = Annotated[
  Optional[bool],
  Field(
    default=None,
    title='Indicator for automatic/non-supervised recording',
    serialization_alias='auto',
  ),
  PlainSerializer(serialize_boolean),
]

SinceField = Annotated[
  Optional[Union[SinceTag, datetime.date, str, int]],
  Field(
    default=None,
    title='Upload date filter',
    description="""
        The since tag allows you to search for recordings that have been uploaded since a certain date. 
        Using a simple integer value such as since:3 will find all recordings uploaded in the past 3 days. 
        If you use a date with a format of YYYY-MM-DD, it will find all recordings uploaded since that date.
        Note that this search considers the upload date, not the date that the recording was made.
        """,
    serialization_alias=aliases.SINCE,
    examples=['2021-12-23'],
  ),
  PlainSerializer(serialize_datetime_date),
]

MethodField = Annotated[
  Optional[RecordingMethod],
  Field(
    default=None,
    title='Method of the recording',
    serialization_alias=aliases.RECORDING_METHOD,
  ),
]
