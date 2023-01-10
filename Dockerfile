FROM python:3

WORKDIR /app

COPY requirements.txt .
COPY entrypoint.sh .

RUN pip3 install -r requirements.txt
RUN chmod +x entrypoint.sh

COPY . .

ENTRYPOINT ["/app/entrypoint.sh"]
