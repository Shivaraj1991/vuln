FROM python:3.15.0rc1-slim-bookworm

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn","myproject.wsgi:application","--bind","0.0.0.0:8000"]
