FROM python:3.8.2-alpine

RUN apk update
RUN apk add --no-cache gcc python3-dev musl-dev

RUN pip install pipenv gunicorn

WORKDIR /usr/src/youtube_api

COPY start.sh start.sh
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pipenv install --system

COPY . .

ENTRYPOINT [ "./start.sh" ]