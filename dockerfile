# Python ka lightweight version use karein
FROM python:3.9-slim

# Working directory set karein
WORKDIR /app

# Files copy karein
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# App run karne ki command
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app