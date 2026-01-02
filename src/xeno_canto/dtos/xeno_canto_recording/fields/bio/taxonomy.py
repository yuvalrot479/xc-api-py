from .....types import Group
from ....constants import aliases
from ..validators import get_validator, validate_string, validate_literal

from typing import Annotated, Optional
from pydantic import Field, BeforeValidator

# --- Taxonomy ---

GenusField = Annotated[
  Optional[str],
  BeforeValidator(get_validator(validate_string, allow_none=True)),
  Field(
    default=None,
    validation_alias=aliases.GENUS,
    description='Generic name of the species',
    examples=['Halcyon'],
  ),
]

EpithetField = Annotated[
  Optional[str],
  BeforeValidator(get_validator(validate_string, allow_none=True)),
  Field(
    default=None,
    validation_alias=aliases.EPITHET,
    description='Specific name (epithet) of the species',
    examples=['smyrnensis'],
  ),
]

SubspeciesField = Annotated[
  Optional[str],
  BeforeValidator(get_validator(validate_string, allow_none=True)),
  Field(
    default=None,
    validation_alias=aliases.SUBSPECIES,
    description='Subspecies epithet.',
    examples=['smyrnensis'],
  ),
]

GroupField = Annotated[
  Optional[Group],
  BeforeValidator(get_validator(validate_literal(Group), allow_none=True)),
  Field(
    default=None,
    validation_alias=aliases.GROUP,
    description='Group to which the species belongs.',
  ),
]

CommonNameField = Annotated[
  Optional[str],
  BeforeValidator(get_validator(validate_string, allow_none=True)),
  Field(
    default=None,
    title='English name of the species',
    validation_alias=aliases.COMMON_NAME,
    examples=['White-throated Kingfisher'],
  ),
]
