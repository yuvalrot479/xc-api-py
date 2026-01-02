from ..search_tag import SearchTag
from ..numeric_tag import NumericTag, NumericRangeTag
import pycountry


class LatitudeTag(NumericTag): ...


class LongitudeTag(NumericTag): ...


class TempTag(NumericRangeTag): ...


class CountryTag(SearchTag):
  def __init__(self, country_identifier: str):
    try:
      country = pycountry.countries.lookup(country_identifier)
      self.country = country

    except Exception:
      raise ValueError(
        f'Invalid country argument "{country_identifier}"; Pass a valid country name or ISO code'
      ) from None


class Box(SearchTag):
  def __init__(self, lat_min: float, lon_min: float, lat_max: float, lon_max: float):
    self.lat_min = lat_min
    self.lon_min = lon_min
    self.lat_max = lat_max
    self.lon_max = lon_max
