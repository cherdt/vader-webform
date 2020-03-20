FROM alpine

RUN apk add --update-cache \
    gcc \
    libc-dev \
    linux-headers \
    musl-dev \
    python3 \
    python3-dev \
  && rm -rf /var/cache/apk/*

COPY ./vader/requirements.txt ./vader/requirements.txt
COPY ./vader/installation.py ./vader/installation.py

WORKDIR /vader

RUN python3 -m venv venv \
  && source venv/bin/activate \
  && pip3 install --requirement requirements.txt \
  && python installation.py

COPY ./vader ./

EXPOSE 9600/tcp

CMD ["/vader/venv/bin/uwsgi", "--http", ":9600", "--mount", "/=vader-web:app"]

