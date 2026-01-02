from ....constants import aliases
from ..validators import get_validator, validate_string, validate_float

from typing import Annotated, Optional
from pydantic import Field, BeforeValidator

# --- Geographic Strings ---

CountryField = Annotated[
  str,
  BeforeValidator(get_validator(validate_string)),
  Field(
    default=None,
    title='Country where the recording was made',
    validation_alias=aliases.COUNTRY,
    examples=['Spain'],
  ),
]

LocalityField = Annotated[
  Optional[str],
  BeforeValidator(get_validator(validate_string, allow_none=True)),
  Field(
    default=None,
    title='Locality where the recording was made',
    validation_alias=aliases.LOCALITY,
    examples=['Sisalde, Ames, A Coruña, Galicia'],
  ),
]

# --- Geospatial / Environmental Floats ---

LatitudeField = Annotated[
  Optional[float],
  BeforeValidator(get_validator(validate_float, allow_none=True)),
  Field(
    default=None,
    title='Latitude of the recording location (degrees)',
    validation_alias=aliases.LATITUDE,
  ),
]

LongitudeField = Annotated[
  Optional[float],
  BeforeValidator(get_validator(validate_float, allow_none=True)),
  Field(
    default=None,
    title='Longitude of the recording location (degrees)',
    validation_alias=aliases.LONGITUDE,
  ),
]

AltitudeField = Annotated[
  Optional[float],
  BeforeValidator(get_validator(validate_float, allow_none=True)),
  Field(
    default=None,
    title='Altitude of the recording location (meters)',
    validation_alias=aliases.ALTITUDE,
  ),
]

TempField = Annotated[
  Optional[float],
  BeforeValidator(get_validator(validate_float, allow_none=True)),
  Field(
    default=None,
    title='Temperature during recording (celsius)',
    validation_alias=aliases.TEMP,
  ),
]
