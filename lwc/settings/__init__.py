import os

from .base import *

if os.environ.get('PRODUCTION', None):
	from .production import *
else:
	from .local import *