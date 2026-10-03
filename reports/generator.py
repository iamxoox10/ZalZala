import json
from pathlib import Path


def save_json(data, filename="zalzala_report.json"):
    output_dir = Path("reports")
    output_dir.mkdir(exist_ok=True)

    output_file = output_dir / filename

    with output_file.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    return str(output_file)
