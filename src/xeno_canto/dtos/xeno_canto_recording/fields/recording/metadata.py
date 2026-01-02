from .....types import XcQualityRating
from ....constants import aliases
from ..validators import (
  get_validator,  # Import your factory
  validate_xc_number,
  validate_string,
  validate_dt_date,
  validate_xc_quality,
  validate_integer,
  validate_dt_timedelta,
)

from typing import Annotated, Optional
from pydantic import Field, BeforeValidator
import datetime

# --- Identity ---

XcNumberField = Annotated[
  int,  # Made non-optional as it's the primary key
  BeforeValidator(get_validator(validate_xc_number, allow_none=False)),
  Field(
    title='Catalogue number of the recording on Xeno Canto',
    validation_alias=aliases.XC_ID,
    examples=[694038],
  ),
]

# --- Metadata Strings ---

MicrophoneField = Annotated[
  Optional[str],
  BeforeValidator(get_validator(validate_string, allow_none=True)),
  Field(
    default=None,
    title='Microphone device model that used to record',
    validation_alias=aliases.MICROPHONE,
  ),
]

DeviceField = Annotated[
  Optional[str],
  BeforeValidator(get_validator(validate_string, allow_none=True)),
  Field(
    default=None,
    title='Recording device model used',
    validation_alias=aliases.DEVICE,
  ),
]

RecordistField = Annotated[
  Optional[str],
  BeforeValidator(get_validator(validate_string, allow_none=True)),
  Field(
    default=None,
    title='Name of the recordist',
    validation_alias=aliases.RECORDIST,
    examples=['Jacobo Ramil Millarengo'],
  ),
]

RemarksField = Annotated[
  Optional[str],
  BeforeValidator(get_validator(validate_string, allow_none=True)),
  Field(
    default=None,
    title='Additional remarks made by the recordist',
    validation_alias=aliases.REMARKS,
    examples=['Male repeating a stereotyped phrase. HPF 270 Hz.'],
  ),
]

# --- Technical & Temporal ---

UploadDateField = Annotated[
  Optional[datetime.date],
  BeforeValidator(get_validator(validate_dt_date, allow_none=True)),
  Field(
    default=None,
    title='Date the recording was uploaded to Xeno Canto',
    validation_alias=aliases.UPLOAD_DATE,
    examples=['2021-12-27'],
  ),
]

SampleRateField = Annotated[
  Optional[int],
  BeforeValidator(get_validator(validate_integer, allow_none=True)),
  Field(
    default=None,
    title='Sample rate of the recording',
    validation_alias=aliases.SAMPLE_RATE,
  ),
]

LengthField = Annotated[
  Optional[datetime.timedelta],
  BeforeValidator(get_validator(validate_dt_timedelta, allow_none=True)),
  Field(
    default=None,
    title='Length of the recording (minutes, seconds)',
    validation_alias=aliases.LENGTH,
    examples=['4:08'],
  ),
]

XcQualityField = Annotated[
  Optional[XcQualityRating],
  BeforeValidator(get_validator(validate_xc_quality, allow_none=True)),
  Field(
    default=None,
    title='Recording quality rating',
    validation_alias=aliases.XC_QUALITY,
  ),
]
