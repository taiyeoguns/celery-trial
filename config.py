from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent

# configuration parameters - http://docs.celeryproject.org/en/latest/userguide/configuration.html

broker_url = config("BROKER_URL", "amqp://guest:guest@localhost:5672//")

result_backend = config("RESULT_BACKEND", "db+sqlite:///results.db")
