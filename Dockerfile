FROM python:3.13.7-slim
LABEL maintainer="taras.mosiichuk.01@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
