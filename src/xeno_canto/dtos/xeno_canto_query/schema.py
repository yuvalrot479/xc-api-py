from .fields.recording.metadata import (
  IdField,
  RecordistField,
  QualityField,
  RemarksField,
  LengthField,
  DeviceField,
  MicrophoneField,
  SampleRateField,
)
from .fields.recording.recording import (
  PlaybackField,
  MethodField,
  SinceField,
  AutomaticField,
)
from .fields.recording.resources import (
  LicenseField,
)
from .fields.bio.taxonomy import (
  GroupField,
  GenusField,
  EpithetField,
  SubspeciesField,
)
from .fields.bio.bio import (
  SoundTypeField,
  SexField,
  LifeStageField,
  BackgroundField,
  SeenField,
  RegistrationField,
)
from .fields.geo.geo import (
  CountryField,
  LocalityField,
  LatitudeField,
  LongitudeField,
  AreaField,
  TempField,
)


from pydantic import BaseModel, ConfigDict
from typing import Optional


class XenoCantoQuerySchema(BaseModel):
  model_config = ConfigDict(arbitrary_types_allowed=True, serialize_by_alias=True)

  genus: GenusField
  epithet: EpithetField
  subspecies: SubspeciesField
  group: GroupField
  recordist: RecordistField
  country: CountryField
  location: LocalityField
  remarks: RemarksField
  seen: SeenField
  playback: PlaybackField
  latitude: LatitudeField
  longitude: LongitudeField
  background: BackgroundField
  sound_type: SoundTypeField
  sex: SexField
  life_stage: LifeStageField
  method: MethodField
  xc_number: IdField
  license: LicenseField
  quality: QualityField
  length: LengthField
  area: AreaField
  since: SinceField
  year: Optional[int] = None
  month: Optional[int] = None
  colyear: Optional[int] = None
  colmonth: Optional[int] = None
  temp: TempField
  registration: RegistrationField
  automatic: AutomaticField
  device: DeviceField
  microphone: MicrophoneField
  sample_rate: SampleRateField
