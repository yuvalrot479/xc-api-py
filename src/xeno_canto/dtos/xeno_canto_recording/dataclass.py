from ...coordinates import Coordinates
from ...patterns import license_pattern
from ...types import (
  SoundType,
  Sex,
  LifeStage,
  RecordingMethod,
)

from dataclasses import (
  dataclass,
  fields,
  field,
)
from typing import (
  Optional,
  List,
  Union,
)
import yarl
import pydantic
import pathlib
import datetime


@dataclass
class XenoCantoRecordingLean:
  number: int
  genus: str
  epithet: str
  common_name: str
  recordist: str
  country: str
  file_name: pathlib.Path
  file_download: yarl.URL
  page: yarl.URL
  license_url: yarl.URL
  upload_date: datetime.date
  length: datetime.timedelta
  quality: str

  sonograms: dict[str, yarl.URL]
  oscillograms: dict[str, yarl.URL]

  @classmethod
  def from_pydantic(cls, m: pydantic.BaseModel):
    class_fields = {f.name for f in fields(cls)}
    data = {k: v for k, v in m.model_dump(exclude_computed_fields=True).items() if k in class_fields}

    return cls(**data)

  @property
  def id(self) -> int:
    return self.number

  @property
  def binomial(self) -> str:
    return self.genus + ' ' + self.epithet

  @property
  def license(self) -> str:
    if match := license_pattern.search(str(self.license_url)):
      d = match.groupdict()
      lic = d.get('license')
      ver = d.get('version')
      return f'{lic},{ver}'
    raise ValueError()


@dataclass
class XenoCantoRecording(XenoCantoRecordingLean):
  date: Optional[datetime.date] = None
  group: Optional[str] = None
  subspecies: Optional[str] = None
  locality: Optional[str] = None
  sound_type: List[SoundType] = field(default_factory=list)
  sex: Optional[Sex] = None
  life_stage: List[LifeStage] = field(default_factory=list)
  seen: Optional[bool] = None
  playback: Optional[bool] = None
  background: List[str] = field(default_factory=list)
  latitude: Optional[float] = None
  longitude: Optional[float] = None
  altitude: Optional[float] = None
  method: Optional[RecordingMethod] = None
  time: Optional[datetime.time] = None
  remarks: Optional[str] = None
  temp: Optional[float] = None
  registration: Optional[Union[int, str]] = None  # Often contains strings in XC
  automatic: Optional[bool] = None
  device: Optional[str] = None
  microphone: Optional[str] = None
  sample_rate: Optional[int] = None

  @property
  def position(self) -> Optional[Coordinates]:
    if self.longitude is not None and self.latitude is not None:
      return Coordinates(
        lon=self.longitude,
        lat=self.latitude,
        alt=self.altitude,
      )
    return None
