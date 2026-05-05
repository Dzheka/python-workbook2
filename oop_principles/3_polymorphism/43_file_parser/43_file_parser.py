import csv
import json
import os
from abc import ABC, abstractmethod


class FileParser(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def parse(self):
        pass

    @abstractmethod
    def validate(self):
        pass

    def get_file_size(self):
        return os.path.getsize(self.file_path)

    def get_extension(self):
        return os.path.splitext(self.file_path)[1]


class CSVParser(FileParser):
    def validate(self):
        return self.file_path.endswith(".csv")

    def parse(self):
        rows = []
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(dict(row))
        return rows


class JSONParser(FileParser):
    def validate(self):
        return self.file_path.endswith(".json")

    def parse(self):
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return None


class FileProcessor:
    def process_file(self, parser):
        return parser.parse()

    def process_batch(self, parsers):
        results = {}
        for parser in parsers:
            results[parser.file_path] = parser.parse()
        return results

    def get_summary(self, parsers):
        total_size = sum(parser.get_file_size() for parser in parsers)
        formats = [parser.get_extension() for parser in parsers]
        return {
            "total": len(parsers),
            "total_size": total_size,
            "formats": formats
        }


def create_parser(file_path):
    ext = os.path.splitext(file_path)[1]
    if ext == ".csv":
        return CSVParser(file_path)
    elif ext == ".json":
        return JSONParser(file_path)
    else:
        raise ValueError(f"Unsupported file format: {ext}")