from decouple import config

# configuration parameters - http://docs.celeryproject.org/en/latest/userguide/configuration.html

broker_url = config("BROKER_URL", "amqp://guest:guest@localhost:5672//")

result_backend = config("RESULT_BACKEND", "db+sqlite:///results.db")
