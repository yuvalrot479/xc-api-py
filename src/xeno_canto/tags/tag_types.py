from typing import Literal, Union

import datetime

Contraint = Literal[
  'exactly',
  'at least',
  'at most',
  'between',
]

Numeric = Union[float, int, datetime.timedelta]
