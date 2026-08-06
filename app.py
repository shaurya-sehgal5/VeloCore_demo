from fastapi import FastAPI
from datetime import datetime
import socket
import os

app = FastAPI(title="VeloCore Demo")

START = datetime.utcnow()

@app.get("/")
def root():
    return {
        "platform": "VeloCore",
        "status": "running",
        "hostname": socket.gethostname()
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/ready")
def ready():
    return {
        "status": "ready"
    }

@app.get("/live")
def live():
    return {
        "status": "alive"
    }

@app.get("/info")
def info():
    return {
        "python": os.sys.version,
        "uptime": str(datetime.utcnow() - START)
    }
