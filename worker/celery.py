import os
from celery import Celery

# for windows
# https://stackoverflow.com/a/53015724
# https://github.com/celery/celery/issues/4178#issuecomment-378075008
os.environ.setdefault("FORKED_BY_MULTIPROCESSING", "1")

# instantiate Celery app object and load config
app = Celery()
app.config_from_object("config")

if __name__ == "__main__":
    app.start()
