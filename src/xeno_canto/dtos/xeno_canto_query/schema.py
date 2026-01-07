from .fields import (
  IdField,
  RecordistField,
  QualityField,
  RemarksField,
  LengthField,
  DeviceField,
  MicrophoneField,
  SampleRateField,
  PlaybackField,
  MethodField,
  SinceField,
  AutomaticField,
  LicenseField,
  GroupField,
  GenusField,
  EpithetField,
  SubspeciesField,
  SoundTypeField,
  SexField,
  LifeStageField,
  BackgroundField,
  SeenField,
  RegistrationField,
  CountryField,
  LocalityField,
  AreaField,
  BoxField,
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
  registration: RegistrationField
  automatic: AutomaticField
  device: DeviceField
  microphone: MicrophoneField
  sample_rate: SampleRateField
  box: BoxField
