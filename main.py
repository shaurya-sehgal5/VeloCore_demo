from fastapi import FastAPI
from datetime import datetime
import socket
import platform
import os
import time

app = FastAPI(
    title="VeloCore Demo",
    version="1.0.0"
)

START_TIME = time.time()


@app.get("/")
def root():
    return {
        "message": "🚀 Running on VeloCore",
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
        "platform": "VeloCore",
        "hostname": socket.gethostname(),
        "python": platform.python_version(),
        "uptime_seconds": round(time.time() - START_TIME, 2),
        "environment": dict(os.environ)
    }
