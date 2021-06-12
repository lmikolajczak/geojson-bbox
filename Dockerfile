FROM python:3.9.5

WORKDIR /code

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH = "${PATH}:/root/.poetry/bin"
# We do not need to create virtualenv inside
# of a docker container
RUN poetry config virtualenvs.create false

# poetry.lock with wildcard because it is
# not always present (copy only if available)
COPY pyproject.toml poetry.lock* /code/
RUN poetry install

CMD tail -f /dev/null
