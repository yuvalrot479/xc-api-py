from ...types import (
  Group,
  SoundType,
  Sex,
  LifeStage,
  RecordingMethod,
)
from ...tags import (
  LengthTag,
  QualityTag,
  SinceTag,
  SampleRateTag,
  CountryTag,
  BoxTag,
)

from typing import TypedDict, Union, List, Tuple
import datetime


class XenoCantoQuery(TypedDict, total=False):
  box: Union[BoxTag, Tuple[float, float, float, float]]
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
  background: List[str]
  sound_type: SoundType
  sex: Sex
  life_stage: LifeStage
  method: RecordingMethod
  xc_number: int
  license: str  # FIXME
  quality: Union[QualityTag, str]
  length: Union[LengthTag, str]
  area: str
  since: Union[SinceTag, str, int, datetime.timedelta]
  year: int
  month: int
  colyear: int
  colmonth: int
  registration: str
  automatic: bool
  device: str
  microphone: str
  sample_rate: Union[SampleRateTag, int, str]
