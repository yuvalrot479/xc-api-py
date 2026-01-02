from typing import Annotated, Optional
import yarl
from pydantic import BeforeValidator, PlainSerializer
from ..validators import validate_url
from ..serializers import serialize_url

UrlField = Annotated[
  Optional[yarl.URL],
  BeforeValidator(validate_url),
  PlainSerializer(serialize_url, return_type=str),
]
