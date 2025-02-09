import os
from time import sleep
import uuid

import requests
from reportlab.pdfgen import canvas

from config import BASE_DIR

from .celery import app


@app.task()
def sometask(x, y):
    return x + y


@app.task(queue="fast")
def fasttask():
    return "Here you go!"


@app.task(queue="slow")
def slowtask(seconds=30):
    if int(seconds) > 60:
        seconds = 60

    # delay initially for 5 seconds
    sleep(5)

    r = requests.get(f"https://misbehaving.site/delay/{seconds}")  # nosec
    return r.status_code


@app.task()
def generate_pdf(text_content):
    task_id = str(uuid.uuid4())
    # Simulate long-running task
    sleep(10)

    # Ensure pdfs directory exists
    documents_directory = BASE_DIR / "pdfs"
    if not os.path.exists(documents_directory):
        os.makedirs(documents_directory)

    # Generate PDF
    filename = f"{str(documents_directory)}/document_{task_id}.pdf"
    c = canvas.Canvas(filename)
    c.drawString(100, 750, "Generated PDF Document")
    c.drawString(100, 700, text_content)
    c.save()

    return {"task_id": task_id, "filename": filename, "status": "completed"}
