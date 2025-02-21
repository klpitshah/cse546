import boto3

DOMAIN_NAME = "1225969188-simpleDB"

sdb = boto3.client("sdb")

sdb.create_domain(DomainName=DOMAIN_NAME)

print(f"SimpleDB domain '{DOMAIN_NAME}' created successfully!")
