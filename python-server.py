from flask import Flask, request, jsonify
import boto3
import os

s3_client = boto3.client("s3", region_name="us-east-2")
sdb = boto3.client("sdb", region_name="us-east-1")

S3_BUCKET = "1225969188-in-bucket"
SIMPLE_DB_DOMAIN = "1225969188-simpleDB"

app = Flask(__name__)

@app.route("/", methods=["POST"])
def upload_file():
    if "inputFile" not in request.files:
        return jsonify({"error": "Missing file with key 'inputFile'"}), 400

    file = request.files["inputFile"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    filename = file.filename
    filename_without_ext, _ = os.path.splitext(file.filename)

    try:
        s3_client.upload_fileobj(file, S3_BUCKET, filename)

        response = sdb.get_attributes(
            DomainName=SIMPLE_DB_DOMAIN,
            ItemName=filename_without_ext,
            AttributeNames=["result"]
        )

        if "Attributes" in response:
            result = response["Attributes"][0]["Value"]
        else:
            result = "Unknown"

        return f"{filename_without_ext}:{result}", 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
