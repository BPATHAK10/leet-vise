import json
from datetime import datetime
from pathlib import Path

class Tracker:
    def _load_all(self):
        if not self.results_file.exists():
            return []
        with open(self.results_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def _save_all(self, data):
        self.results_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.results_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
