from .....types import Group
from ....constants import aliases

from typing import Annotated, Optional
from pydantic import Field

GenusField = Annotated[
  Optional[str],
  Field(
    default=None,
    title='Generic name of the species',
    serialization_alias=aliases.GENUS,
    description=r"Genus is part of a species' scientific name, so it is searched by default when performing a basic search. But you can use the gen tag to limit your search query only to the genus field. These fields use a 'starts with' query and accept a 'matches' operator.",
    examples=['[halcyon] smyrnensis smyrnensis'],
  ),
]

EpithetField = Annotated[
  Optional[str],
  Field(
    default=None,
    title='Specific name (epithet) of the species',
    serialization_alias=aliases.EPITHET,
    examples=['halcyon [smyrnensis] smyrnensis'],
  ),
]

SubspeciesField = Annotated[
  Optional[str],
  Field(
    default=None,
    title='Subspecies epithet.',
    serialization_alias=aliases.SUBSPECIES,
    examples=['halcyon smyrnensis [smyrnensis]'],
  ),
]

GroupField = Annotated[
  Optional[Group],
  Field(
    default=None,
    title='Group to which the species belongs.',
    serialization_alias=aliases.GROUP,
    description=r'Use the grp tag to narrow down your search to a specific group. Valid group values are birds, grasshoppers, bats, frogs and land mammals. You can also use their respective ids (1 to 5).',
  ),
]
