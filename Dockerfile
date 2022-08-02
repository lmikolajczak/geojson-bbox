FROM python:3.10

WORKDIR /code

# Install Poetry
ENV POETRY_VERSION=1.1.14
RUN curl -sSL https://install.python-poetry.org | python - --version $POETRY_VERSION
# Add poetry install location to PATH
ENV PATH=/root/.local/bin:$PATH

# We do not need to create virtualenv inside of a docker container
RUN poetry config virtualenvs.create false

# poetry.lock with wildcard because it is not always present (copy only if available)
COPY pyproject.toml poetry.lock* /code/
RUN poetry install

CMD tail -f /dev/null
