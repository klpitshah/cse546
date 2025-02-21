from flask import Flask, request, jsonify
import boto3
import os


s3_client = boto3.client("s3")
sdb = boto3.client("sdb")

app = Flask(__name__)

@app.route("/", methods=["POST"])
def upload_file():
    if "inputFile" not in request.files:
        return jsonify({"error": "Missing file with key 'inputFile'"}), 400

    file = request.files["inputFile"]
    
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    try:
        # Upload file to S3
        s3_client.upload_fileobj(file, "1225969188-in-bucket" , file.filename)

        response = sdb.get_attributes(
            DomainName="1225969188-simpleDB",
            ItemName=filename,
            AttributeNames=["result"]
        )

        if "Attributes" in response:
            result = response["Attributes"][0]["Value"]
        else:
            result = "Unknown"

        return f"{filename}:{result}", 200
    except Exception as e:
        return "error" + e, 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
