FROM python:3.12.12-alpine

ARG GPIO_GID

WORKDIR /app

RUN apk update && \
    apk add --no-cache py3-libgpiod 

COPY requirements.txt .

RUN python -m venv .venv
RUN source .venv/bin/activate
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000/tcp

CMD ["python", "-m", "blink"]
