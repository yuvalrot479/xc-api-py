from xeno_canto import Client
from dotenv import dotenv_values
from rich import print
import time
import random

env = dotenv_values()
api_key = env.get('XC_API_KEY')
if not api_key:
  raise RuntimeError()

client = Client(api_key, verbose=True)
rs = client.search(binomial='Canis aureus', limit=30)
client.download(rs)  # type: ignore
