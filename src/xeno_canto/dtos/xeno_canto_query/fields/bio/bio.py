from .....types import Sex, LifeStage, SoundType
from ....constants import aliases

from typing import Annotated, List, Union, Optional
from pydantic import Field


SexField = Annotated[
  Optional[Sex],
  Field(
    default=None,
    title='Sex of the recorded animal',
    serialization_alias=aliases.SEX,
  ),
]

LifeStageField = Annotated[
  Optional[Union[LifeStage, List[LifeStage]]],
  Field(
    default=None,
    title='Life stage of the recorded animal',
    serialization_alias=aliases.LIFE_STAGE,
  ),
]

SoundTypeField = Annotated[
  Optional[SoundType],
  Field(
    default=None,
    title='Call type of the recorded animal',
    serialization_alias=aliases.SOUND_TYPE,
  ),
]

BackgroundField = Annotated[
  Optional[List[str]],
  Field(
    default=None,
    title='Background species identified in the recording',
    serialization_alias=aliases.BACKGROUND_SPECIES,
    examples=[['Turdus viscivorus', 'Parus major']],
  ),
]

RegistrationField = Annotated[
  Optional[str],
  Field(
    default=None,
    title='Registration number (if specimen collected)',
    serialization_alias=aliases.REG_NUMBER,
  ),
]

SeenField = Annotated[
  Optional[bool],
  Field(
    default=None,
    title='Recorded animal was seen by the recordist',
    serialization_alias=aliases.ANIMAL_SEEN,
  ),
]
