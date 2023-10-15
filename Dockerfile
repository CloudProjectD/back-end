FROM python:3.10

ENV PYTHONUNBUFFERED 1

EXPOSE 8000
WORKDIR /app

COPY . .
RUN pip install -r requirements.txt

CMD	uvicorn --host=0.0.0.0 app.main:app
