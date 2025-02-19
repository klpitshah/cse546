from flask import Flask, request, jsonify
import boto3
import os


s3_client = boto3.client("s3")


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

        return jsonify({"message": "File uploaded successfully", "filename": file.filename}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to upload file: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
