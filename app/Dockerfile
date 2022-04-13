FROM python:3.10-slim as build

ENV VENV_PATH=/opt/venv
ENV POETRY_VERSION=1.1.12 \
    POETRY_VIRTUALENVS_CREATE=false \
    PATH="$VENV_PATH/bin:/root/.local/bin:$PATH"

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential curl gcc python3-dev libssl-dev gettext locales git libpq-dev \
    && locale-gen && apt-get autoclean && apt-get autoremove --yes && rm -rf /var/lib/{apt,dpkg,cache,log}/ \
    && curl -sSL https://install.python-poetry.org | python -
RUN python -m venv $VENV_PATH
COPY poetry.lock pyproject.toml ./
RUN pip install --upgrade pip && . $VENV_PATH/bin/activate && poetry install --no-interaction -vv
RUN find $VENV_PATH -name '__pycache__' -exec rm -Rf {} +

FROM python:3.10-slim


RUN apt-get update && \
    apt-get install -y --no-install-recommends libssl-dev gettext locales libpq-dev netcat-openbsd && \
    locale-gen && apt-get autoclean && apt-get autoremove --yes && rm -rf /var/lib/{apt,dpkg,cache,log}/

ENV VENV_PATH=/opt/venv
ENV PYTHONUNBUFFERED=1 \
    PATH="$VENV_PATH/bin:$PATH"
WORKDIR /app
COPY --from=build $VENV_PATH $VENV_PATH
COPY . .
EXPOSE 80
CMD python manage.py migrate && python manage.py collectstatic --noinput && python manage.py loaddata fixtures/initital.json; gunicorn --chdir /app example.wsgi:application -b :80 -w 1 --threads 8
