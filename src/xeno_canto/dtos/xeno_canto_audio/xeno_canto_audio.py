from ...types import XcQualityRating
from .errors import AudioNotLoadedError

from dataclasses import dataclass, field
from pathlib import Path
from typing import (
  Optional,
  Union,
  Iterator,
  Self,
  Any,
)
import warnings
import miniaudio
import numpy as np
from datetime import timedelta
from functools import partial
from contextlib import contextmanager
from uuid import uuid4
from dataclasses import is_dataclass
from pydantic import BaseModel
from requests import Session


@dataclass
class XenoCantoAudio:
  binomial: Optional[str] = None
  subspecies: Optional[str] = None
  number: Optional[int] = None
  recordist: Optional[str] = None
  name: Optional[str] = None
  quality: Optional[XcQualityRating] = None
  sample_rate: Optional[int] = field(default=None, repr=True, metadata={'units': 'Hz'})
  fmt: Optional[str] = None

  _bytes_promise: Optional[partial[bytes]] = field(default=None, init=False, repr=False)
  _original_file: Optional[Path] = field(default=None, init=False, repr=False)
  _data: Optional[bytes] = field(default=None, init=False, repr=False)
  _decoded: Optional[miniaudio.DecodedSoundFile] = field(default=None, init=False, repr=False)

  _NORM: float = field(default=32768.0, init=False, repr=False)

  @contextmanager
  def load(self) -> Iterator[Self]:
    """Context manager to decode audio into memory."""
    try:
      if self._decoded is not None:
        yield self
        return

      if self._bytes_promise:
        # Fetch remote bytes and decode
        raw_bytes = self._bytes_promise()
        # miniaudio.decode requires bytes; target_sr is the file's SR
        self._decoded = miniaudio.decode(raw_bytes)

      elif self._original_file:
        self._decoded = miniaudio.decode_file(str(self._original_file))

      else:
        raise RuntimeError('No source provided (file or URL)')

      yield self
    finally:
      self._decoded = None

  @classmethod
  def from_record(cls, r: Any, promise: Optional[partial[bytes]] = None) -> Self:
    if isinstance(r, BaseModel) or is_dataclass(r):
      name = r.file_name  # type: ignore
      number = r.number  # type: ignore
      recordist = r.recordist  # type: ignore
      quality = r.quality  # type: ignore
      sample_rate = r.sample_rate  # type: ignore
      file_dl = r.file_download  # type: ignore
      binomial = r.binomial  # type: ignore
      subspecies = r.subspecies  # type: ignore
      fmt = 'wav'  # FIXME

    elif isinstance(r, dict):
      name = r['file_name']
      number = r['number']
      recordist = r['recordist']
      quality = r['quality']
      sample_rate = r['sample_rate']
      file_dl = r['file_download']
      binomial = r['genus'] + ' ' + r['epithet']
      subspecies = r.get('subspecies', None)
      fmt = 'wav'  # FIXME

    else:
      raise ValueError(r)

    obj = cls(
      name=name,
      number=number,
      recordist=recordist,
      quality=quality,
      sample_rate=sample_rate,
      binomial=binomial,
      subspecies=subspecies,
      fmt=fmt,
    )

    if promise:
      obj._bytes_promise = partial(promise, file_dl)

    return obj

  @classmethod
  def from_file(cls, path: Union[str, Path]) -> Self:
    path = Path(path)
    if not path.exists():
      raise FileNotFoundError(path)

    obj = cls(name=path.name)
    obj._original_file = path
    return obj

  # --- Methods ---

  def to_numpy(self, start: Optional[timedelta] = None, length: Optional[timedelta] = None) -> np.ndarray:
    if self._decoded is None:
      raise AudioNotLoadedError()

    # Access raw 16-bit buffer
    arr = np.frombuffer(self._decoded.samples, dtype=np.int16).reshape(-1, self._decoded.nchannels)

    sr = self.sample_rate
    if sr is None:
      raise RuntimeError()

    start_idx = int(start.total_seconds() * sr) if start else 0  # type: ignore

    if start_idx >= len(arr):
      raise ValueError(f'Start index {start_idx} exceeds audio length {len(arr)}')

    if length:
      end_idx = start_idx + int(length.total_seconds() * sr)
      arr = arr[start_idx:end_idx]
    else:
      arr = arr[start_idx:]

    return (arr.astype(np.float32) / self._NORM).copy()

  def to_birdnet(self, start: Optional[timedelta] = None, length: Optional[timedelta] = None) -> np.ndarray:
    arr = self.to_numpy(start=start, length=length)

    # Downmix to Mono
    if arr.ndim > 1 and arr.shape[1] > 1:
      arr = arr.mean(axis=1)
    else:
      arr = arr.flatten()

    if self.sample_rate != 48000:
      warnings.warn(f'Sample rate is {self.sample_rate}; BirdNET requires 48000Hz for optimal results.')

    return arr

  def save(self, directory: Optional[Union[Path, str]] = None, name: Optional[str] = None):
    if self._data is None:
      if self._bytes_promise is None:
        raise ValueError()
      self._data = self._bytes_promise()

    out_dir = Path(directory) if directory else Path.cwd()
    out_dir.mkdir(parents=True, exist_ok=True)

    target_path = out_dir / (name or self.name or f'recording-{uuid4()}.{self.fmt}')

    target_path.write_bytes(self._data)  # type: ignore
