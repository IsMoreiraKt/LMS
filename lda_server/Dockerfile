FROM python:3.13-alpine

ENV PYTHONUNBUFFERED=1 \
    FLASK_ENV=production \
    FLASK_APP=app.py

RUN apk add --no-cache gcc musl-dev libffi-dev

WORKDIR /flask_app
COPY lda_server /flask_app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 1354

CMD ["gunicorn", "--bind", "0.0.0.0:1354", "app:app"]