import csv


def test_read_csv_data():
    with open("/Users/inderpreetsingh/PycharmProjects/Playwrightpythonproject_RS/test_results.csv",newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Status'] == "Failed" or row['Status'] == "Skipped":
                print(f"{row['TestCaseID']}")