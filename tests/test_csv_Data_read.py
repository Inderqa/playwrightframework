import csv
from pathlib import Path
csv_path = Path(__file__).parent.parent / "test_results.csv"
def test_read_csv_data():
    with open(csv_path,newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Status'] == "Failed" or row['Status'] == "Skipped":
                print(f"{row['TestCaseID']}")
