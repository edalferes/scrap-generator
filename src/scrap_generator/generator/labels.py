# src/scrap_generator/generator/labels.py

import random


class LabelGenerator:
    def __init__(self, labels_count: int):
        self.labels_count = labels_count

    def generate_labels(self, idx: int) -> str:
        labels = [f'label{i}=\"val{random.randint(0, 100)}\"' for i in range(
            self.labels_count)]
        labels.append(f'series_id=\"{idx}\"')
        return ",".join(labels)
