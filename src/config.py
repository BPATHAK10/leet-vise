import os
from dotenv import load_dotenv

load_dotenv()

NOTION_API_TOKEN = os.getenv("NOTION_API_TOKEN")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")
TIMER_MINUTES = 15
CACHE_FILE = "data/cache.json"
ONLY_BLIND_75 = True
