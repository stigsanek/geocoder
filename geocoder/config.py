import os
from pathlib import Path

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent.parent
LOGS_DIR = ROOT_DIR / 'logs'
CSV_DIR = ROOT_DIR / 'csv'

load_dotenv(ROOT_DIR / '.env')

API_KEY = os.getenv('API_KEY')
IS_REVERSE = bool(int(os.getenv('IS_REVERSE')))
