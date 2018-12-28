import os
from dotenv import load_dotenv
load_dotenv()

# configuration parameters - http://docs.celeryproject.org/en/latest/userguide/configuration.html

broker_url = os.getenv('BROKER_URL') or 'amqp://guest:guest@localhost:5672//'

result_backend = os.getenv('RESULT_BACKEND') or 'db+sqlite:///results.db'