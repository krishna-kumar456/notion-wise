import logging
import uvicorn

from .email import send_email
from fastapi import FastAPI, BackgroundTasks

app = FastAPI(title="Notion Wise")

@app.get("/")
def read_root():
    return {"NotionWise": "Success"}


@app.get("/send-notification")
async def send_email_notification_task(background_tasks: BackgroundTasks):
    """ Sends email notification for random notes.

    Repeats every 24 hours.
    """

    print("Begin send_email_notification_task")
    background_tasks.add_task(send_email)
    print("End send_email ")



   


