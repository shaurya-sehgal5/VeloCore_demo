import streamlit as st
import psutil
import time
import random
from datetime import datetime

st.set_page_config(
    page_title="VeloCore Demo",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 VeloCore Deployment Demo")
st.caption("Self-Hosted Kubernetes Platform")

cpu, mem, disk, req = st.columns(4)

cpu.metric(
    "CPU",
    f"{psutil.cpu_percent()}%"
)

mem.metric(
    "Memory",
    f"{psutil.virtual_memory().percent}%"
)

disk.metric(
    "Disk",
    f"{psutil.disk_usage('/').percent}%"
)

req.metric(
    "Requests",
    random.randint(1200, 4200)
)

st.divider()

st.subheader("Recent Deployment Events")

logs = [
    "Repository cloned",
    "Dependencies installed",
    "Docker image built",
    "Security scan passed",
    "Image pushed",
    "Kubernetes deployment created",
    "Pods are Ready",
    "Ingress configured",
    "Deployment successful"
]

for log in logs:
    st.success(f"{datetime.now().strftime('%H:%M:%S')}   {log}")

st.divider()

st.subheader("Runtime Health")

st.progress(random.randint(70,100))

st.code("""
STATUS      : RUNNING
FRAMEWORK   : Streamlit
RUNTIME     : Kubernetes
SECURITY    : PASSED
HEALTH      : HEALTHY
""")

st.caption("Powered by VeloCore 🚀")
