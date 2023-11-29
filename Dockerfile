FROM python:3.10.7-alpine3.16 as builder

WORKDIR /app
ENV PATH="/app/venv/bin:$PATH"
COPY requirements.txt .

RUN apk add postgresql-dev gcc python3-dev musl-dev

RUN python -m venv /app/venv

RUN pip install -r requirements.txt

FROM python:3.10.7-alpine3.16

RUN addgroup app_user && adduser -S app_user -u 1000 -G app_user

WORKDIR /app
ENV PATH="/app/venv/bin:$PATH"

RUN apk update \
	&& apk -U upgrade \
	&& apk add --no-cache ca-certificates bash gcc libpq-dev \
	&& update-ca-certificates --fresh \
	&& rm -rf /var/cache/apk/*

COPY --from=builder /app/venv /app/venv
COPY --chown=app_user:app_user . .

USER app_user

ENTRYPOINT ["app-entrypoint"]