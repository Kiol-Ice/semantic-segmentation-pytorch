FROM python:3.10.9-slim

WORKDIR /app

COPY requirements.txt /app

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY flask /app/flask
EXPOSE 8080

CMD ["python", "flask/server.py"]