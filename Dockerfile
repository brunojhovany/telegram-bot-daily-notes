FROM --platform=arm64 golang:1.21.1-alpine3.18 AS builder

WORKDIR /app

COPY pkiller.go .

RUN go build pkiller.go

FROM --platform=arm64 python:3.9.5-alpine3.13

WORKDIR /app

COPY --from=builder /app/pkiller .

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY config.py config.py
COPY app.py app.py
COPY job_controls.bash job_controls.bash

RUN apk add --no-cache curl bash

RUN mkdir /notes

# create a user to run the app
RUN adduser -D telegram

# change ownership of our app
RUN chown -R telegram:telegram /app
RUN chown -R telegram:telegram /notes

# change to this new user
USER telegram

# run the app

CMD [ "/bin/bash", "-c", "./job_controls.bash" ]
# CMD [ "python", "app.py" ]

