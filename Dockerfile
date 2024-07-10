FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY wait-for-it.sh .
COPY init-db.sh /docker-entrypoint-initdb.d/init-db.sh
COPY specific_tables.sql /docker-entrypoint-initdb.d/specific_tables.sql

CMD ["./wait-for-it.sh", "postgres:5432", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]
