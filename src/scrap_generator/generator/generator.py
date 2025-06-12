# generator/generator.py

import threading
import random
from .labels import LabelGenerator
from ..config import Settings


class MetricsGenerator:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.series_count = settings.series_count
        self.metric_name = settings.metric_name
        self.labels = LabelGenerator(self.settings.labels_count)
        self.series_labels = {}
        self.series = []

        self.generate_series()

    def generate_series(self):
        for i in range(self.series_count):
            label_str = self.labels.generate_labels(i)
            self.series_labels[i] = label_str
            static_value = 100
            self.series.append(
                f"{self.metric_name}{{{label_str}}} {static_value}")

    def get_metrics(self):
        if self.settings.static_values:
            return "\n".join(self.series) + "\n"

        result = []
        for i in range(self.series_count):
            label_str = self.series_labels[i]
            value = random.random() * 100
            result.append(f"{self.metric_name}{{{label_str}}} {value}")
        return "\n".join(result) + "\n"
