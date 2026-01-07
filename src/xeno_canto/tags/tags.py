from ..types import XcQualityRating
from .search_tag import SearchTag
from .numeric_tag import NumericTag, NumericRangeTag
from .types import Numeric, Contraint, Box

from typing import (
  Union,
  Optional,
  overload,
  Any,
  Tuple,
)
import datetime
import pycountry
from pycountry.db import Country
from ..coordinates import Coordinates


class CountryTag(SearchTag):
  def __init__(self, country_identifier: str):
    try:
      ct: Country = pycountry.countries.lookup(country_identifier)  # type: ignore

    except Exception:
      raise ValueError(
        f'Invalid country argument "{country_identifier}"; Pass a valid country name or ISO code'
      ) from None

    self.name = ct.name.lower()
    self.alpha_2 = ct.alpha_2.lower()
    self.alpha_3 = ct.alpha_3.lower()


class BoxTag(SearchTag):
  @overload
  def __init__(self, box: Box): ...

  @overload
  def __init__(self, west: Tuple[float, float], east: Tuple[float, float]): ...

  @overload
  def __init__(self, west: Coordinates, east: Coordinates): ...

  @overload
  def __init__(self, lat_min: float, lon_min: float, lat_max: float, lon_max: float): ...

  def __init__(self, *args: Any):  # type: ignore
    if len(args) == 1:
      # Case 1: Box object
      box = args[0]
      self.ay, self.ax = box[0], box[1]
      self.by, self.bx = box[2], box[3]

    elif len(args) == 2 and all(isinstance(arg, Coordinates) for arg in args):
      # Case 2: Two Coordinate objects (West and East)
      west, east = args
      self.ay, self.ax = west.lat, west.lon
      self.by, self.bx = east.lat, east.lon

    elif len(args) == 2 and all(isinstance(arg, tuple) for arg in args):
      west, east = args
      self.ay, self.ax = west
      self.by, self.bx = east

    elif len(args) == 4:
      self.ay, self.ax, self.by, self.bx = args

    else:
      raise TypeError('Invalid arguments provided to BoxTag')


class LengthTag(NumericRangeTag): ...


class SampleRateTag(NumericTag): ...


class QualityTag(NumericRangeTag):
  def assign(self, f: str, v: Union[str, int]):
    try:
      if isinstance(v, str):
        self.a = XcQualityRating[v.capitalize()]
      else:
        self.a = XcQualityRating(v)
      setattr(self, f, v)

    except ValueError:
      values = ', '.join([f'"{r.name}"' for r in XcQualityRating])
      raise ValueError(
        (
          f'Invalid quality "{v}";',
          'Pass one of the following (case-insensitive): ',
          values,
        )
      )

  def __init__(
    self,
    a: Union[str, int],
    b: Optional[Union[str, int]] = None,
    constraint: Optional[Contraint] = None,
  ):
    self.assign('a', a)
    if b is not None:
      self.assign('b', b)
    self.constraint = constraint

  @classmethod
  def between(cls, a: Union[str, int], b: Union[str, int]):
    raise NotImplementedError()  # TODO

  @classmethod
  def at_least(cls, v: Union[str, int]):
    return cls(v, constraint='at least')  # f'">{value}"'

  @classmethod
  def at_most(cls, v: Union[str, int]):
    return cls(v, constraint='at most')  # f'"<{value}"'


class SinceTag(SearchTag):
  def __init__(self, value: Union[Numeric, datetime.datetime]):
    self.value = value
