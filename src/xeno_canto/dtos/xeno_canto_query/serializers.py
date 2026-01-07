from ...tags import (
  BoxTag,
  CountryTag,
  QualityTag,
)
from ...tags.numeric_tag import NumericTag

import datetime


def serialize_numeric_tag(v):
  if isinstance(v, NumericTag):
    match v.constraint:
      case 'at least':
        return f'">{v.a}"'
      case 'at most':
        return f'"<{v.a}"'
      case 'exactly':
        return f'"={v.a}"'
      case 'between':
        return f'"{v.a}-{v.b}"'
      case _:
        return f'{v.a}'

  return v


def serialize_boolean(v):
  if isinstance(v, bool):
    return 'yes' if v else 'no'
  return v


def serialize_datetime_date(v):
  if isinstance(v, datetime.date):
    return v.isoformat()
  return v


def serialize_country(v):
  if isinstance(v, CountryTag):
    return v.name
  return v


def serialize_box(v):
  if isinstance(v, BoxTag):
    return f'{v.ay},{v.ax},{v.by},{v.bx}'

  elif isinstance(v, tuple):
    ay, ax, by, bx = v
    return f'{ay},{ax},{by},{bx}'

  return v
