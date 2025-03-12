import asyncio
import time


def synk_send_email():
    time.sleep(3)
    print("Email was sent")
    return "Email was sent"

async def async_send_email():
    await asyncio.sleep(3)
    print("Async Email was sent")
    return "Async Email was sent"


