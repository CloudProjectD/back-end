FROM python:3.10

ENV PYTHONUNBUFFERED 1

EXPOSE 8000
WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN pip install poetry==1.0.* && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY . ./

CMD alembic upgrade head && \
    uvicorn --host=0.0.0.0 app.main:app
