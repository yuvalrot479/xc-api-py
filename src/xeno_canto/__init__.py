"""Xeno-Canto API"""

__version__ = '0.1.0'

from .client.client import Client
from . import tags

__all__ = ['Client', 'tags']
