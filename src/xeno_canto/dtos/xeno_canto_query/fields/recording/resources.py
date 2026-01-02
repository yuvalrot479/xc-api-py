from ....constants import aliases

from typing import Annotated, Optional
from pydantic import Field

LicenseField = Annotated[
  Optional[str],
  Field(
    default=None,
    description="""
        Recordings on xeno-canto are licensed under a small number of different Creative Commons licenses.
        You can search for recordings that match specific license conditions using the lic tag.
        License conditions are Attribution (BY), NonCommercial (NC), ShareAlike (SA), NoDerivatives (ND) and Public Domain/copyright free (CC0).
        Conditions should be separated by a '-' character.
        For instance, to find recordings that are licensed under an Attribution-NonCommercial-ShareAlike license, use lic:BY-NC-SA;
        for "no rights reserved" recordings, use lic:PD.
        See the Creative Commons website for more details about the individual licenses.
        """,
    serialization_alias=aliases.LICENSE,
  ),
]
