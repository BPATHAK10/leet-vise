import json
from pathlib import Path
from src.config import CACHE_FILE

class CacheManager:
    def __init__(self, cache_file=CACHE_FILE):
        self.cache_file = Path(cache_file)

    def load_cache(self):
        if not self.cache_file.exists():
            return {}
        with open(self.cache_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_cache(self, data):
        self.cache_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.cache_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
