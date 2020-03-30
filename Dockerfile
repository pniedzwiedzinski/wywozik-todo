FROM python:3.8-alpine

RUN pip3 install requests

WORKDIR /app

COPY main.py /app

CMD ["python", "/app/main.py"]
