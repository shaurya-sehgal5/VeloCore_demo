FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
CMD wget -qO- http://127.0.0.1:8000/health || exit 1

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]
