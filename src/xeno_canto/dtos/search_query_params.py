from .xeno_canto_query import XenoCantoQuery
from ..client.types import ReturnMode

from typing import TypedDict, List


class SearchQueryParams(XenoCantoQuery, TypedDict, total=False):
  binomial: str
  species_list: List[str]
  limit: int
  mode: ReturnMode
  lean: bool
  stream: bool
