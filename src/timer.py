import threading
import time
from rich.console import Console

console = Console()

class TimerThread(threading.Thread):
    def __init__(self, seconds):
        super().__init__()
        self.seconds = seconds
        self._running = True
        self.time_left = seconds

    def run(self):
        first_tick = True
        while self.time_left > 0 and self._running:
            mins, secs = divmod(self.time_left, 60)
             # Only add a newline on the first print so the timer starts on its own line
            if first_tick:
                console.print(f"\n⏱  {mins:02d}:{secs:02d}", end="\r")
                first_tick = False
            else:
                console.print(f"⏱  {mins:02d}:{secs:02d}", end="\r")
            time.sleep(1)
            self.time_left -= 1

        if self._running and self.time_left == 0:
            console.print("\n⏰ Time's up!            ")

    def stop(self):
        self._running = False
