from .celery import app
from time import sleep
import requests

@app.task()
def sometask(x, y):
    return x + y

@app.task(queue='fast')
def fasttask():
    return "Here you go!"

@app.task(queue='slow')
def slowtask(seconds=30):
    if int(seconds) > 60:
        seconds = 60
    
    # delay initially for 5 seconds
    sleep(5)

    r = requests.get(f'https://misbehaving.site/delay/{seconds}')
    return r.status_code
