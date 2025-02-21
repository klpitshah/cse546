import boto3
import csv
import os

SIMPLE_DB_DOMAIN = "1225969188-simpleDB"
CSV_FILE = "dataset.csv"

sdb = boto3.client("sdb", region_name="us-east-1")

def upload_to_simpledb():
    try:
        with open(CSV_FILE, "r") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)

            for row in reader:
                filename_with_ext, prediction = row[0], row[1]
                filename, _ = os.path.splitext(filename_with_ext)

                sdb.put_attributes(
                    DomainName=SIMPLE_DB_DOMAIN,
                    ItemName=filename,
                    Attributes=[{"Name": "result", "Value": prediction, "Replace": True}]
                )
                print(f"Uploaded {filename} -> {prediction}")

        print("All data uploaded successfully!")

    except Exception as e:
        print(f"Error: {str(e)}")

upload_to_simpledb()
