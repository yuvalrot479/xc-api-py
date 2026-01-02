from ....constants import aliases
from ..validators import get_validator, validate_url, validate_string
from ..serializers import serialize_url
from .sonograms import SonogramsSchema
from .oscillograms import OscillogramsSchema

from typing import Annotated, Optional
from pydantic import Field, BeforeValidator, PlainSerializer
import yarl


SonogramsField = Annotated[
  Optional[SonogramsSchema],
  Field(
    default=None,
    title='URLs of the recording sonograms',
    validation_alias='sono',
  ),
]

OscillogramsField = Annotated[
  Optional[OscillogramsSchema],
  Field(
    default=None,
    title='URLs of the recording oscillograms',
    validation_alias='osci',
  ),
]
LicenseUrlField = Annotated[
  Optional[yarl.URL],
  BeforeValidator(get_validator(validate_url, allow_none=True)),
  Field(
    default=None,
    title='URL describing the license of this recording',
    validation_alias=aliases.LICENSE,
  ),
  PlainSerializer(serialize_url, return_type=str),
]

XcPageField = Annotated[
  Optional[yarl.URL],
  BeforeValidator(get_validator(validate_url, allow_none=True)),
  Field(
    default=None,
    title='URL specifying the details of this recording',
    validation_alias=aliases.PAGE_URL,
  ),
  PlainSerializer(serialize_url, return_type=str),
]

FileDownloadField = Annotated[
  Optional[yarl.URL],
  BeforeValidator(get_validator(validate_url, allow_none=True)),
  Field(
    default=None,
    title='(base) URL to the audio file',
    validation_alias=aliases.FILE,
  ),
  PlainSerializer(serialize_url, return_type=str),
]

FileNameField = Annotated[
  Optional[str],
  BeforeValidator(get_validator(validate_string, allow_none=True)),
  Field(
    default=None,
    title='Original file name of the audio file',
    validation_alias=aliases.FILE_NAME,
  ),
]
