from ...types import (
  Group,
  SoundType,
  Sex,
  LifeStage,
  RecordingMethod,
)
from ...tags.geo import (
  TempTag,
  CountryTag,
  LatitudeTag,
  LongitudeTag,
)
from ...tags.meta import (
  LengthTag,
  QualityTag,
  RecordingNumberTag,
  SinceTag,
  SampleRateTag,
)

from typing import TypedDict, Union, List
import datetime


class XenoCantoQuery(TypedDict, total=False):
  genus: str
  epithet: str
  subspecies: str
  group: Group
  common_name: str
  recordist: str
  country: Union[CountryTag, str]
  location: str
  remarks: str
  seen: bool
  playback: bool
  latitude: Union[LatitudeTag, float]
  longitude: Union[LongitudeTag, float]
  background: List[str]
  sound_type: SoundType
  sex: Sex
  life_stage: LifeStage
  method: RecordingMethod
  xc_number: Union[RecordingNumberTag, int]
  license: str  # FIXME
  quality: Union[QualityTag, str]
  length: Union[LengthTag, str]
  area: str
  since: Union[SinceTag, str, int, datetime.timedelta]
  year: int
  month: int
  colyear: int
  colmonth: int
  temp: Union[TempTag, str, float]
  registration: str
  automatic: bool
  device: str
  microphone: str
  sample_rate: Union[SampleRateTag, int, str]
