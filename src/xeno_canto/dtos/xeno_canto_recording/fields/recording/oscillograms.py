from .common import UrlField

from pydantic import (
  BaseModel,
  ConfigDict,
  Field,
)


class OscillogramsSchema(BaseModel):
  model_config = ConfigDict(
    arbitrary_types_allowed=True,
  )

  small: UrlField = Field(default=None)
  medium: UrlField = Field(default=None, validation_alias='med')
  large: UrlField = Field(default=None)
