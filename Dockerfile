FROM python:3.9-alpine3.13
LABEL maintainer="rojpadida.herokuapp.com"

ENV PYTHONBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./app /app
COPY ./scripts /scripts

WORKDIR /app
EXPOSE 8082

RUN python -m venv /py
RUN /py/bin/pip install --upgrade pip
RUN apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev linux-headers
RUN /py/bin/pip install -r /requirements.txt
RUN apk del  .tmp-deps
RUN adduser --disabled-password --no-create-home app && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R app:app /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

USER app

CMD ["_run.sh"]