from flask import Flask, jsonify
import socket
import time

app = Flask(__name__)
start = time.time()

@app.get("/")
def home():
    return jsonify({
        "platform": "VeloCore",
        "status": "running",
        "hostname": socket.gethostname()
    })

@app.get("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.get("/ready")
def ready():
    return jsonify({"status": "ready"}), 200

@app.get("/live")
def live():
    return jsonify({"status": "alive"}), 200

@app.get("/info")
def info():
    return jsonify({
        "uptime": round(time.time() - start, 2)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
