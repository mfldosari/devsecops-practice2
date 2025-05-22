FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip setuptools && pip install -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]
