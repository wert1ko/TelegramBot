from fastapi import FastAPI, HTTPException
from schemas.message_data import MessageData
from aiogram import Bot
from config import settings

app = FastAPI()
bot = Bot(token=settings.bot.BOT_TOKEN)


@app.post("/bot/send_to_channel")
async def send_to_channel(data: MessageData):
    try:
        message_text = (
            f"Full name: {data.full_name}\n"
            f"Phone number: {data.phone_number}\n"
            f"Comment: {data.comment}"
        )
        await bot.send_message(settings.bot.CHANNEL_ID, message_text)
        return {"status": "Message sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
