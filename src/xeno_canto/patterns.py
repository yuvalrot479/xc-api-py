import re


license_pattern = re.compile(r'/licenses/(?P<license>[a-z-]+)/(?P<version>\d+\.\d+)/')
float_pattern = re.compile(r'([-+]?\d*\.?\d+)')
xc_upload_url_pattern = re.compile(
  (
    r'^https?://xeno-canto\.org/sounds/uploaded'
    r'/(?P<user_id>[^/]+)'
    r'/(?:ffts|wave)'  # "ffts"=sonogram, "wave"=oscillogram
    r'/XC(?P<recording_id>\d+)'
    r'-(?P<version>small|med|large|full)'
    r'\.(?P<file_ext>[a-z0-9]+)$'
  )
)
partial_date_pattern = re.compile(r'^(?P<year>\d{4})-(?P<month>\d{2})-00$')  # YYYY-MM-00 or YYYY-00-00
