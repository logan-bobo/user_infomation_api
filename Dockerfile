FROM python:3.10.4

ENV POETRY_VERSION=1.1.0

RUN pip3 install "poetry==$POETRY_VERSION"

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi
    
COPY src/ .

CMD ["./main.py"]


