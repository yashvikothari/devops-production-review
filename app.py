from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "application": "DevOps Production Review",
        "status": "running",
        "version": "1.0"
    })

@app.get("/health")
def health():
    return jsonify({"status": "healthy"}), 200
