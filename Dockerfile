FROM python:3.11.0b1-slim-buster


COPY . /app

WORKDIR /app

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install nginx python3-dev \
    && apt-get -y install build-essential

RUN pip install -r requirements.txt --src /usr/local/src

COPY nginx.conf /etc/nginx

RUN chmod +x ./start.sh

CMD ["./start.sh"]
