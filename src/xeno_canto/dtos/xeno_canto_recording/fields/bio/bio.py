from ....constants import aliases
from ..validators import (
  get_validator,
  validate_string,
  validate_literal_list,
  validate_string_list,
  validate_boolean,
)
from .types import Sex, LifeStage, SoundType

from typing import Annotated, List, Optional
from pydantic import Field, BeforeValidator

SexField = Annotated[
  List[Sex],
  BeforeValidator(get_validator(validate_literal_list(Sex), allow_none=True, default_factory=list)),
  Field(
    default=None,
    title='Sex of the recorded animal',
    validation_alias=aliases.SEX,
  ),
]

LifeStageField = Annotated[
  List[LifeStage],
  BeforeValidator(get_validator(validate_literal_list(LifeStage), default_factory=list)),
  Field(
    default_factory=list,
    title='Life stage of the recorded animal',
    validation_alias=aliases.LIFE_STAGE,
  ),
]

SoundTypeField = Annotated[
  List[SoundType],
  BeforeValidator(get_validator(validate_literal_list(SoundType), default_factory=list)),
  Field(
    default_factory=list,
    title='Call type of the recorded animal',
    validation_alias=aliases.SOUND_TYPE,
  ),
]

# --- Recording Context ---

BackgroundField = Annotated[
  List[str],
  BeforeValidator(get_validator(validate_string_list, default_factory=list)),
  Field(
    default_factory=list,
    title='Background species identified in the recording',
    validation_alias=aliases.BACKGROUND_SPECIES,
    examples=[['Turdus viscivorus', 'Parus major']],
  ),
]

RegistrationField = Annotated[
  Optional[str],
  BeforeValidator(get_validator(validate_string, allow_none=True)),
  Field(
    default=None,
    validation_alias=aliases.REG_NUMBER,
    description='Registration number (if specimen collected)',
  ),
]

SeenField = Annotated[
  Optional[bool],
  BeforeValidator(get_validator(validate_boolean, allow_none=True)),
  Field(
    default=None,
    description='Recorded animal was seen by the recordist',
    validation_alias=aliases.ANIMAL_SEEN,
  ),
]
