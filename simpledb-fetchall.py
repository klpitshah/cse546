import boto3

SIMPLE_DB_DOMAIN = "1225969188-simpleDB"

sdb = boto3.client("sdb", region_name="us-east-1")

response = sdb.select(
    SelectExpression=f"select * from `{SIMPLE_DB_DOMAIN}` limit 10"
)

for item in response.get("Items", []):
    print(f"Item: {item['Name']}")
    for attr in item.get("Attributes", []):
        print(f"  {attr['Name']}: {attr['Value']}")

print("Query completed.")
