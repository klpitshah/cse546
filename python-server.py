from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def upload_file():
    if "inputFile" not in request.files:
        return jsonify({"error": "Missing file with key 'inputFile'"}), 400

    file = request.files["inputFile"]
    
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    # Process the file (for now, just returning its name)
    return jsonify({"message": "File received", "filename": file.filename}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
