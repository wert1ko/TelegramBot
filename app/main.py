from fastapi import FastAPI, HTTPException
from schemas.message_data import MessageData
from aiogram import Bot
from fastapi.middleware.cors import CORSMiddleware
from config import settings

app = FastAPI()
bot = Bot(token=settings.bot.BOT_TOKEN)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/bot/send_to_channel")
async def send_to_channel(data: MessageData):
    try:
        message_text = (
            f"Ім'я та прізвище: {data.full_name}\n"
            f"Пошта: {data.email}\n"
            f"Номер телефону: {data.phone_number}\n"
            f"Рід діяльності: {data.type_of_activity}"
        )
        await bot.send_message(settings.bot.CHANNEL_ID, message_text)
        return {"status": "Message sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
