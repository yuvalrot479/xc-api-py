from ...types import XcQualityRating
from ..search_tag import SearchTag
from ..numeric_tag import NumericTag, NumericRangeTag
from ..tag_types import Numeric, Contraint

from typing import Union, Optional
import datetime


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


class RecordingNumberTag(NumericRangeTag):
  @classmethod
  def at_least(cls, v: Numeric):  # HACK
    raise NotImplementedError()

  @classmethod
  def at_most(cls, v: Numeric):  # HACK
    raise NotImplementedError()

  @classmethod
  def exactly(cls, v: Numeric):  # HACK
    raise NotImplementedError()
