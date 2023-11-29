FROM python:3.10.7-alpine3.16 as builder

WORKDIR /app

COPY requirements.txt .

RUN apk add postgresql-dev gcc python3-dev musl-dev

RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

FROM python:3.10.7-alpine3.16

RUN addgroup app_user && adduser -S app_user -u 1000 -G app_user

WORKDIR /backend

RUN apk update \
	&& apk -U upgrade \
	&& apk add --no-cache ca-certificates bash gcc libpq-dev \
	&& update-ca-certificates --fresh \
	&& rm -rf /var/cache/apk/*

COPY --chown=klever:klever --from=builder /app/wheels /wheels
COPY --chown=klever:klever --from=builder /app/requirements.txt .
RUN pip install --no-cache /wheels/*

COPY --chown=app_user:app_user . .
RUN chown -R app_user:app_user .

USER app_user

ENTRYPOINT ["python"]