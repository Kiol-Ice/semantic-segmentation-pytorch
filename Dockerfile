FROM python:3.10.9-slim

WORKDIR /app

COPY requirements.txt /app

RUN python -m pip install --upgrade pip 
RUN pip install -r requirements.txt

COPY . /app
RUN python init.py

EXPOSE 80

CMD ["python", "server.py"]