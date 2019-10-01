import os
from pathlib import Path

_ROOT_PATH = Path(os.path.abspath(os.path.dirname(__file__)))
_DATA_PATH = _ROOT_PATH / 'data'

from .bible_books import BibleBooks
from .settings import BIBLE_API_KEY
from .bible import Bible
from .bible_factory import BibleFactory



