from flask import Flask, request, jsonify
import requests
import os
import json

app = Flask(__name__)

WEB3_STORAGE_TOKEN = "YOUR_WEB3_STORAGE_API_TOKEN"   #use your API Token

def upload_to_ipfs(file_path):
    headers = {
        "Authorization": f"Bearer {WEB3_STORAGE_TOKEN}",
    }
    with open(file_path, "rb") as f:
        files = {"file": (os.path.basename(file_path), f)}
        response = requests.post("https://api.web3.storage/upload", headers=headers, files=files)
    return response.json()["cid"]

@app.route("/upload", methods=["POST"]) 
def upload():
    name = request.form["name"]
    level = request.form["level"]
    image = request.files["image"]

    image_path = f"temp_{name}.png"
    image.save(image_path)
    image_cid = upload_to_ipfs(image_path)

    metadata = {
        "name": name,
        "description": f"Level {level} character",
        "image": f"https://{image_cid}.ipfs.w3s.link/{image.filename}",
        "attributes": [{"trait_type": "Level", "value": int(level)}]
    }

    metadata_path = f"temp_{name}.json"
    with open(metadata_path, "w") as f:
        json.dump(metadata, f)

    metadata_cid = upload_to_ipfs(metadata_path)
    os.remove(image_path)
    os.remove(metadata_path)

    token_uri = f"https://{metadata_cid}.ipfs.w3s.link/{os.path.basename(metadata_path)}"
    return jsonify({"tokenURI": token_uri})

if __name__ == "__main__":
    app.run(debug=True)
