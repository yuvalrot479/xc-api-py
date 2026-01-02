from .....types import RecordingMethod
from ....constants import aliases
from ..validators import get_validator, validate_boolean, validate_dt_date, validate_dt_time, validate_literal

from typing import Annotated, Optional
from pydantic import Field, BeforeValidator
import datetime


PlaybackField = Annotated[
  Optional[bool],
  BeforeValidator(get_validator(validate_boolean, allow_none=True)),
  Field(
    title='Playback was used to lure the animal.',
    validation_alias=aliases.PLAYBACK_USED,
  ),
]

AutomaticField = Annotated[
  Optional[bool],
  BeforeValidator(get_validator(validate_boolean, allow_none=True)),
  Field(
    title='Indicator for automatic/non-supervised recording',
    validation_alias=aliases.AUTOMATIC,
  ),
]

RecordedDateField = Annotated[
  Optional[datetime.date],
  BeforeValidator(get_validator(validate_dt_date, allow_none=True)),
  Field(
    title='Date the recording was made',
    validation_alias=aliases.RECORDED_DATE,
    examples=['2021-12-23'],
  ),
]

RecordedTimeField = Annotated[
  Optional[datetime.time],
  BeforeValidator(get_validator(validate_dt_time, allow_none=True)),
  Field(
    title='Time of day when the recording was made',
    validation_alias=aliases.RECORDED_TIME,
    examples=['09:30'],
  ),
]

MethodField = Annotated[
  Optional[RecordingMethod],
  BeforeValidator(get_validator(validate_literal(RecordingMethod), allow_none=True)),
  Field(
    title='Method of the recording',
    validation_alias=aliases.RECORDING_METHOD,
  ),
]
