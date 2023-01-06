FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt .
COPY entrypoint.sh .

RUN pip3 install -r requirements.txt --no-cache-dir
RUN chmod +x entrypoint.sh

COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]