import yarl
import datetime
from typing import Any
from ..types import QualityRating


def serialize_yarl(v: Any) -> Any:
  if isinstance(v, yarl.URL):
    return str(v)
  return v


def serialize_quality_rating(v: Any) -> Any:
  if isinstance(v, QualityRating):
    return v.name
  return v


def serialize_datetime_date(v: Any) -> Any:
  if isinstance(v, datetime.date):
    return v.isoformat()
  return v
