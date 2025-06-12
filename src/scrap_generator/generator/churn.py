# src/scrap_generator/generator/churn.py

import threading
import time


class ChurnManager:
    def __init__(self, generator, interval: int):
        self.generator = generator
        self.interval = interval
        if self.interval > 0:
            threading.Thread(target=self.run_churn_loop, daemon=True).start()

    def run_churn_loop(self):
        while True:
            time.sleep(self.interval)
