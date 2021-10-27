FROM python:3.7-alpine

EXPOSE 8080/tcp

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py .

COPY count.txt .

COPY -r /templates/. .

CMD ["python", "./main.py"]
