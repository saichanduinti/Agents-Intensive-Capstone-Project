import datetime
import sys

class Logger:
    def __init__(self):
        self.logs = []

    def log(self, message: str):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] {message}"
        self.logs.append(entry)
        print(entry, file=sys.stdout)

logger = Logger()
