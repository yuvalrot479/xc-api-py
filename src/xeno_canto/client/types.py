from ..dtos.xeno_canto_query import XenoCantoQuerySchema
from ..dtos.xeno_canto_recording import (
  XenoCantoRecordingSchema,
  XenoCantoRecording,
  XenoCantoRecordingLean,
  XenoCantoRecordingLeanSchema,
)
from ..dtos.xeno_canto_audio import XenoCantoAudio

from typing import (
  Union,
  Dict,
  Any,
  Literal,
)

Category = Literal[
  'binomial',
  'author',
]

ReturnMode = Literal[
  'dataclass',
  'dict',
  'json',
  'pydantic',
  'audio',
]


Record = Union[
  str,  # JSON
  Dict[str, Any],
  XenoCantoRecordingSchema,
  XenoCantoRecording,
  XenoCantoRecordingLean,
  XenoCantoRecordingLeanSchema,
  XenoCantoAudio,
]

Query = Union[
  Dict[str, Any],
  XenoCantoQuerySchema,
]

RecordingId = Union[str, int]
