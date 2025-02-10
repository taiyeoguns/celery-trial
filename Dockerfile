FROM python:3.12-slim-bookworm

ENV LANG=C.UTF-8

ENV APP_DIR=/usr/src/app

RUN apt-get update -y \
    && apt-get install --no-install-recommends libpq-dev gcc -y \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p ${APP_DIR} \
    && useradd --create-home appusr

# Make app as working directory
WORKDIR ${APP_DIR}

# Install requirements
COPY requirements.txt ${APP_DIR}
RUN pip install --no-cache-dir --upgrade pip -r requirements.txt \
    && chown -R appusr:appusr ${APP_DIR}
USER appusr

# Copy rest of application files to app folder
COPY . ${APP_DIR}
