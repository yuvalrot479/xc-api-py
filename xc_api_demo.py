from xc_api import (
  Client,
  SearchQuery,
  RecordingAudio,
  tags,
)
from dotenv import dotenv_values
from datetime import timedelta
import pandas as pd
import sounddevice as sd
import random

api_key = dotenv_values('.env')['XC_API_KEY']
if not api_key:
  raise RuntimeError()

if __name__ == '__main__':
  """
  First step: instanciate the client with your Xeno Canto API key
  """
  client = Client('Replace with your XC API key')
  client = Client(api_key)

  """
  Example query #1
  - Recorded in Israel
  - Quality is at least 'B' (on a A-E scale)
  - At least 10 seconds long
  - Uploaded to Xeno Canto in the past 50 weeks
  """
  query_1 = SearchQuery(
    recording_country=tags.Country('israel'),
    recording_quality=tags.Quality.at_least('B'),
    recording_length=tags.Length.at_least(timedelta(seconds=10)),
    recording_since=tags.since(timedelta(weeks=50)),
  )

  """
  Example query #2:
  - Genus is Acrocephalus
  - Recorded in Europe
  - Animal was seen during recording
  - Not an automatic recording
  - Length is between 30 and 60 seconds
  """
  query_2 = SearchQuery(
    animal_genus='acrocephalus',
    recording_area='europe',
    recording_animal_seen=True,
    recording_automatic=False,
    recording_length=tags.Length.between(30, 60),
  )

  """
  Example query #3:
  - Recorded in the area between Maine and New-Brunswick
  - Quality is 'A'
  - Sound type is "song"
  - Recorded in the month of May (any year)
  """
  query_3 = SearchQuery(
    recording_box=tags.Box(
      45.319105511767994, -69.72746227713218,
      47.60054859752724, -65.26321586868441,
    ),
    recording_quality=tags.Quality('A'),
    recording_month=5
  )

  """
  Example query #4:
  - Animal group is "grasshoppers"
  - Temperature during recording was at least 25°C
  - Animal is an adult (life stage)
  """
  query_4 = SearchQuery(
    animal_group='grasshoppers',
    recording_temp=tags.Temp.at_least(25),
    animal_life_stage='adult',
  )

  queries = [query_1, query_2, query_3, query_4]

  """
  You can use your queries by passing them to .find_recordings();
  
  IMPORTANT:
  This will return a generator, which is a one-time consumed object;
  Once iterated over, it becomes exhausted and will yield no further results.
  
  To use the results multiple times, wrap the function call in list();
  Also, you may pass a non-negative limit argument to the function call.
  """
  random_query = random.choice(queries)

  for recording in client.find(random_query):
    ...
  
  recordings = list(client.find(random_query, limit=5))

  """
  In addition to querying, you can retrieve recordings by specifying their XC catalogue number;
  If the catalogue number does not exist, it will return None;
  
  You may pass the 'XC' prefix (case-insensitive) if you'd like to;
  """
  recording_1 = client.get_by_id('102121')
  recording_2 = client.get_by_id('xc140047')
  recording_3 = client.get_by_id('XC178864')

  """
  Loading recordings into Pandas DataFrame can be done by
   converting recording objects to dictionaries with .model_dump();
  Then we can load them into a DataFrame with .from_records()
  """
  df = pd.DataFrame.from_records([r.model_dump() for r in recordings])
  print(df)
  
  """
  You can load recordings into RecordingAudio objects by
   calling its factory class method .from_recording() on them.
  """
  audios = [ RecordingAudio.from_recording(r) for r in recordings ]

  """
  To interact with actual audio files, call .load() on a RecordingAudio object;
  This will essentially download the remote audio file and load it into memory;
  
  After loading, you can interact with it by calling .to_numpy() or .to_birdnet():
  
  .to_numpy() will return a normalized NumPy array 
  
  .to_birdnet() will return the same as above but compatible with BirdNET;
  
  IMPORTANT:
  BirdNET expects a 48000Khz sample rate
  """
  for audio in audios:
    with audio.load() as a:
      # Full recording
      full = a.to_numpy()
      
      # Extracted 5-second segment, starting from 0:01
      seg = a.to_numpy(
        start=timedelta(seconds=1), # Optional
        length=timedelta(seconds=5) # Optional
      )
      
      # BirdNET compatible array
      bn_arr = a.to_birdnet()
      
      # Recording sample rate
      sr = a.sample_rate
      
      """
      Example usage: playing with SoundDevice
      """
      print(f'Playing {a}')
      sd.play(seg, sr)
      sd.wait()
  
  """
  You can save the original audio files locally,
   by calling .save() on RecordingAudio objects;
  """
  [a.save() for a in audios]