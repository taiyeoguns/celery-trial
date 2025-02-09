import os

from celery.result import AsyncResult
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, RedirectResponse
from pydantic import BaseModel

from worker.tasks import generate_pdf

app = FastAPI()


class TextContent(BaseModel):
    content: str


@app.get("/", include_in_schema=False)
def home():
    return RedirectResponse(url="/docs")


@app.post("/generate-pdf/")
async def create_pdf(text_content: TextContent):
    task = generate_pdf.delay(text_content.content)
    return {"task_id": task.id}


@app.get("/pdf-status/{task_id}")
async def get_pdf_status(task_id: str):
    task_result = AsyncResult(task_id)
    return {
        "task_id": task_id,
        "status": task_result.status,
        "result": task_result.result if task_result.ready() else None,
    }


@app.get("/download-pdf/{task_id}")
async def download_pdf(task_id: str):
    task_result = AsyncResult(task_id)

    if not task_result.ready():
        raise HTTPException(status_code=404, detail="PDF is still being generated")

    result = task_result.result
    if not result or "filename" not in result:
        raise HTTPException(status_code=404, detail="PDF not found")

    filename = result["filename"]
    if not os.path.exists(filename):
        raise HTTPException(status_code=404, detail="PDF file not found")

    return FileResponse(
        filename, media_type="application/pdf", filename=os.path.basename(filename)
    )
