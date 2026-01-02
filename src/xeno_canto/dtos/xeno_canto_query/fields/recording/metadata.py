from .....types import XcQualityRating
from .....tags.meta import SampleRateTag, RecordingNumberTag
from ....constants import aliases
from ..serializers import (
  serialize_recording_number,
  serialize_sample_rate,
)

from typing import Annotated, Union, Optional
from pydantic import Field, PlainSerializer
import datetime

IdField = Annotated[
  Optional[Union[RecordingNumberTag, int]],
  Field(
    default=None,
    title='Catalogue number of the recording on Xeno Canto',
    description="""
        All recordings on xeno-canto are assigned a unique catalog number (generally displayed in the form XC76967).
        To search for a known recording number, use the nr tag: for example nr:76967.
        You can also search for a range of numbers as nr:88888-88890.
        """,
    serialization_alias=aliases.XC_NUMBER,
    examples=[694038],
  ),
  PlainSerializer(serialize_recording_number),
]

MicrophoneField = Annotated[
  Optional[str],
  Field(
    default=None,
    title='Microphone device model that used to record',
    serialization_alias=aliases.MICROPHONE,
  ),
]

DeviceField = Annotated[
  Optional[str],
  Field(
    default=None,
    title='Recording device model used',
    serialization_alias=aliases.DEVICE,
  ),
]

SampleRateField = Annotated[
  Optional[Union[SampleRateTag, int]],
  Field(
    default=None,
    title='Sample rate of the recording',
    serialization_alias=aliases.SAMPLE_RATE,
  ),
  PlainSerializer(serialize_sample_rate),
]

RecordistField = Annotated[
  Optional[str],
  Field(
    default=None,
    title='Name of the recordist',
    description=r"To search for all recordings from a particular recordist, use the rec tag. For example, rec:John will return all recordings from recordists whose names contain the string \"John\". This field accepts a 'matches' operator.",
    serialization_alias=aliases.RECORDIST,
    examples=['Jacobo Ramil Millarengo'],
  ),
]

RemarksField = Annotated[
  Optional[str],
  Field(
    default=None,
    title='Additional remarks made by the recordist',
    serialization_alias=aliases.REMARKS,
    examples=['Male repeating a stereotyped phrase. HPF 270 Hz.'],
  ),
]

LengthField = Annotated[
  Optional[Union[datetime.timedelta, int, str]],
  Field(
    default=None,
    title='Length of the recording (minutes, seconds)',
    serialization_alias=aliases.LENGTH,
    examples=['4:08'],
  ),
]

QualityField = Annotated[
  Optional[Union[XcQualityRating, str]],
  Field(
    default=None,
    title='Recording quality rating',
    serialization_alias=aliases.XC_QUALITY,
  ),
]
