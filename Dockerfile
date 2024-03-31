FROM python:3.10.9-slim

WORKDIR /app

COPY requirements.txt /app

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

COPY . /app
EXPOSE 8080

CMD ["python", "server.py"]