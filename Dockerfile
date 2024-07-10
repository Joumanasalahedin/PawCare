FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY wait-for-it.sh .


CMD ["./wait-for-it.sh", "postgres:5432", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]
