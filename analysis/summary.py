"""Print the reported BUS227 results.

These are the percentages reported in the presentation — not raw
survey rows. The raw survey data is not available (student email
closed), so this script only reproduces the reported summary.
"""
import csv
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "data" / "reported_results.csv"

with path.open(newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(f"{row['metric']}: {row['value']}  ({row['note']})")
