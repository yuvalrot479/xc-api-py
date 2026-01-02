from .fields.recording.metadata import (
  XcNumberField,
  RecordistField,
  XcQualityField,
  RemarksField,
  LengthField,
  UploadDateField,
  DeviceField,
  MicrophoneField,
  SampleRateField,
)
from .fields.recording.recording import (
  PlaybackField,
  MethodField,
  AutomaticField,
  RecordedDateField,
  RecordedTimeField,
)
from .fields.recording.resources import (
  SonogramsField,
  OscillogramsField,
  LicenseUrlField,
  XcPageField,
  FileDownloadField,
  FileNameField,
)
from .fields.bio.taxonomy import (
  GroupField,
  GenusField,
  EpithetField,
  SubspeciesField,
  CommonNameField,
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
  AltitudeField,
  TempField,
)
from ...dtos.coordinates import Coordinates
from ...patterns import license_pattern


from pydantic import BaseModel, ConfigDict, computed_field
from typing import Optional


class XenoCantoRecordingLeanSchema(BaseModel):
  model_config = ConfigDict(
    arbitrary_types_allowed=True,
    populate_by_name=True,  # Essential for XC API tag mapping
  )
  number: XcNumberField
  genus: GenusField
  epithet: EpithetField
  common_name: CommonNameField
  recordist: RecordistField
  country: CountryField
  file_name: FileNameField
  file_download: FileDownloadField
  page: XcPageField
  license_url: LicenseUrlField
  upload_date: UploadDateField
  length: LengthField
  quality: XcQualityField

  sonograms: SonogramsField
  oscillograms: OscillogramsField

  @computed_field
  def id(self) -> int:
    if self.number:
      return self.number
    raise ValueError()

  @computed_field
  def binomial(self) -> str:
    if self.genus and self.epithet:
      return f'{self.genus} {self.epithet}'
    return 'Unknown species'

  @computed_field
  def license(self) -> Optional[str]:
    if self.license_url:
      match = license_pattern.search(str(self.license_url))
      if match:
        d = match.groupdict()
        return f'{d.get("license")},{d.get("version")}'
    return None


class XenoCantoRecordingSchema(XenoCantoRecordingLeanSchema):
  date: RecordedDateField
  group: GroupField
  subspecies: SubspeciesField
  locality: LocalityField
  sound_type: SoundTypeField
  sex: SexField
  life_stage: LifeStageField
  seen: SeenField
  playback: PlaybackField
  background: BackgroundField
  latitude: LatitudeField
  longitude: LongitudeField
  altitude: AltitudeField
  temp: TempField
  method: MethodField
  time: RecordedTimeField
  remarks: RemarksField
  registration: RegistrationField
  automatic: AutomaticField
  device: DeviceField
  microphone: MicrophoneField
  sample_rate: SampleRateField

  @computed_field
  def position(self) -> Optional[Coordinates]:
    if self.longitude is not None and self.latitude is not None:
      return Coordinates(
        lon=self.longitude,
        lat=self.latitude,
        alt=self.altitude,
      )
    return None
