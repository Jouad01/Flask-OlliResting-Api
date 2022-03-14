FROM python:3.9-slim
LABEL Jouad El Ouardi "jouardiouardi@cifpfbmoll.eu"

RUN apt-get update -y && \
    apt-get install -y gcc libmariadb3 libmariadb-dev

EXPOSE 8000/udp
EXPOSE 8000/tcp

# Copiar requeriments
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT flask run --host=0.0.0.0 --port=8000