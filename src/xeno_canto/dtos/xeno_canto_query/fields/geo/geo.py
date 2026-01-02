from .....tags.geo import TempTag, CountryTag
from ....constants import aliases
from .....types import Area
from ..serializers import (
  serialize_temp,
  serialize_country,
)

from typing import Annotated, Union, Optional
from pydantic import Field, PlainSerializer

CountryField = Annotated[
  Optional[Union[CountryTag, str]],
  Field(
    default=None,
    title='Country where the recording was made',
    serialization_alias=aliases.COUNTRY,
    examples=['Spain'],
  ),
  PlainSerializer(serialize_country),
]

LocalityField = Annotated[
  Optional[str],
  Field(
    default=None,
    title='Locality where the recording was made',
    serialization_alias=aliases.LOCALITY,
    examples=['Sisalde, Ames, A Coruña, Galicia'],
  ),
]

LatitudeField = Annotated[
  Optional[float],
  Field(
    default=None,
    title='Latitude of the recording location (degrees)',
    serialization_alias=aliases.LATITUDE,
  ),
]

LongitudeField = Annotated[
  Optional[float],
  Field(
    default=None,
    title='Longitude of the recording location (degrees)',
    serialization_alias=aliases.LONGITUDE,
  ),
]

TempField = Annotated[
  Optional[Union[TempTag, str, float, int]],
  Field(
    default=None,
    title='Temperature during recording (celsius)',
    serialization_alias=aliases.TEMP,
  ),
  PlainSerializer(serialize_temp),
]

AreaField = Annotated[
  Optional[Area],
  Field(
    default=None,
    description='The area tag allows you to search by world area. Valid values for this tag are africa, america, asia, australia, europe.',
    serialization_alias=aliases.AREA,
  ),
]
