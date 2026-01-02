# from ...types import QualityRating
from ....tags.meta import (
  RecordingNumberTag,
  SampleRateTag,
)
from ....tags.geo import (
  TempTag,
  CountryTag,
)

import yarl
import datetime
from typing import Any
import re


def serialize_boolean(v):
  if isinstance(v, bool):
    return 'yes' if v else 'no'
  return v


def serialize_datetime_date(v):
  if isinstance(v, datetime.date):
    return v.isoformat()
  return v


def serialize_recording_number(v):
  if isinstance(v, RecordingNumberTag):
    ...  # FIXME
  return v


def serialize_sample_rate(v):
  if isinstance(v, SampleRateTag):
    ...  # FIXME
  return v


def serialize_temp(v):
  if isinstance(v, TempTag):
    ...  # FIXME
  return v


def serialize_country(v):
  if isinstance(v, CountryTag):
    ...  # FIXME
  return v


# def serialize_yarl(v: Any) -> Any:
#   if isinstance(v, yarl.URL):
#     return str(v)
#   return v


# def serialize_quality_rating(v: Any) -> Any:
#   if isinstance(v, QualityRating):
#     return v.name
#   return v


# def serialize_datetime_date(v: Any) -> Any:
#   if isinstance(v, datetime.date):
#     return v.isoformat()
#   return v


# def serialize_license(v: Any) -> Any:
#   if isinstance(v, yarl.URL):
#     if match := LICENSE_PATTERN.search(str(v)):
#       d = match.groupdict()
#       lic = d.get('license')
#       ver = d.get('version')
#       return f'{lic},{ver}'
