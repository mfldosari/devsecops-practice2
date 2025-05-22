# Dockerfile for Flask App
#
# Builds a minimal Python 3.11 Flask application container for DevSecOps practice.
#
# Usage:
#   docker build -t flask-app .

FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip setuptools && pip install -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]
