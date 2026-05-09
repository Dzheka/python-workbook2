from abc import ABC, abstractmethod
import os
import csv
import json

class FileParser(ABC):
    def __init__(self, file_path: str):
        self.file_path = file_path

    @abstractmethod
    def parse(self):
        pass

    @abstractmethod
    def validate(self) -> bool:
        pass

    def get_file_size(self) -> int:
        try:
            return os.path.getsize(self.file_path)
        except FileNotFoundError:
            return 0

    def get_extension(self) -> str:
        return os.path.splitext(self.file_path)[1]


class CSVParser(FileParser):
    def validate(self) -> bool:
        return self.get_extension().lower() == ".csv"

    def parse(self):
        if not self.validate():
            raise ValueError("Invalid file format for CSVParser")
        data = []
        try:
            with open(self.file_path, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    data.append(row)
        except Exception as e:
            print(f"Error parsing CSV: {e}")
        return data


class JSONParser(FileParser):
    def validate(self) -> bool:
        return self.get_extension().lower() == ".json"

    def parse(self):
        if not self.validate():
            raise ValueError("Invalid file format for JSONParser")
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            print(f"Malformed JSON: {e}")
            return {}
        except Exception as e:
            print(f"Error parsing JSON: {e}")
            return {}


class FileProcessor:
    def process_file(self, parser: FileParser):
        return parser.parse()

    def process_batch(self, parsers):
        results = {}
        for parser in parsers:
            results[parser.file_path] = parser.parse()
        return results

    def get_summary(self, parsers):
        return {
            "total": len(parsers),
            "total_size": sum(p.get_file_size() for p in parsers),
            "formats": [p.get_extension().lstrip(".") for p in parsers],
        }


def create_parser(file_path: str) -> FileParser:
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".csv":
        return CSVParser(file_path)
    elif ext == ".json":
        return JSONParser(file_path)
    else:
        raise ValueError(f"Unsupported file format: {ext}")
    

# Create parsers for different formats
csv_parser = CSVParser("data/users.csv")
json_parser = JSONParser("data/config.json")

# Parse files polymorphically
print("=== CSV Parsing ===")
csv_data = csv_parser.parse()
print(f"Parsed {len(csv_data)} records from CSV")
if csv_data:
    print(f"First record: {csv_data[0]}")
# Output:
# Parsed 3 records from CSV
# First record: {'name': 'Alice', 'age': '30', 'city': 'NYC'}

print("\n=== JSON Parsing ===")
json_data = json_parser.parse()
print(f"JSON data: {json_data}")
# Output:
# JSON data: {'app': 'MyApp', 'version': '1.0', 'debug': True}

# Validation
print("\n=== File Validation ===")
parsers = [csv_parser, json_parser]
for parser in parsers:
    is_valid = parser.validate()
    print(f"{parser.get_extension()} file valid: {is_valid}")
# Output:
# .csv file valid: True
# .json file valid: True

# File information
print("\n=== File Information ===")
for parser in parsers:
    print(f"File: {parser.file_path}")
    print(f"  Extension: {parser.get_extension()}")
    print(f"  Size: {parser.get_file_size()} bytes")
# Output:
# File: data/users.csv
#   Extension: .csv
#   Size: 245 bytes
# File: data/config.json
#   Extension: .json
#   Size: 128 bytes

# Using FileProcessor
processor = FileProcessor()

# Process single file
print("\n=== Processing Single File ===")
data = processor.process_file(csv_parser)
print(f"Processed data: {data}")

# Process batch of files polymorphically
print("\n=== Batch Processing ===")
all_parsers = [csv_parser, json_parser]
results = processor.process_batch(all_parsers)
print(f"Processed {len(results)} files")
for file_path, data in results.items():
    print(f"  {file_path}: {type(data).__name__}")
# Output:
# Processed 2 files
#   data/users.csv: list
#   data/config.json: dict

# Get summary statistics
print("\n=== Processing Summary ===")
summary = processor.get_summary(all_parsers)
print(f"Total files: {summary['total']}")
print(f"Total size: {summary['total_size']} bytes")
print(f"Formats: {summary['formats']}")
# Output:
# Total files: 2
# Total size: 256 bytes
# Formats: ['csv', 'json']

# Auto-detect parser type
print("\n=== Auto-Detection ===")
parser1 = create_parser("data/users.csv")
parser2 = create_parser("data/config.json")

print(f"Auto-detected: {type(parser1).__name__}")  # CSVParser
print(f"Auto-detected: {type(parser2).__name__}")  # JSONParser

# Error handling
try:
    invalid_parser = create_parser("data/file.txt")
except ValueError as e:
    print(f"\nError: {e}")
# Output: Error: Unsupported file format: .txt