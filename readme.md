# Celery Trial

Simple setup of [Celery](http://www.celeryproject.org/) task queue to execute long running jobs asynchronously.

## Requirements

-   Python 3.12
-   [Celery](http://www.celeryproject.org/)
-   [RabbitMQ](https://www.rabbitmq.com/)
-   [Redis](https://www.redis.io)

## Installation

### Clone Project

```sh
git clone https://github.com/taiyeoguns/celery-trial.git
```

### Install Requirements

With a [virtualenv](https://virtualenv.pypa.io/) already set up, install the requirements with pip:

```sh
pip install -r requirements-dev.txt
```

### Add details in `.env` file

Create `.env` file from example file and maintain necessary details in it e.g. Broker URL, Results backend

```sh
cp .env.example .env
```

Otherwise, skip to use the default settings which require RabbitMQ as Broker and SQLite as Results backend.

### Start the worker

Open a terminal window and start the default Celery worker by running:

```sh
celery worker -A worker.tasks -l info
```

For routing to queue specific workers for handling tasks of different execution times, run:

```sh
celery worker -A worker.tasks -Q slow -l info
```
```sh
celery worker -A worker.tasks -Q fast -l info
```

### Run tasks
Open a python shell and run the tasks:

```py
from worker.tasks import sometask, slowtask, fasttask
res = slowtask.delay()
```

Check status:
```py
res.status
```

Get result after completion
```py
res.get()
```

## Tests

Run:

```sh
pytest -vv
```

### Run application with Docker

With Docker and Docker Compose set up, run:

```sh
docker-compose up --build
```

Wait till setup is complete and all containers are started.

Thereafter, application to show PDF generation handled in queue should be available at `http://localhost:8000`
