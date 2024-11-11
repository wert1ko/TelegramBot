from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


class BOT_SETTINGS(BaseSettings):
    BOT_TOKEN: str = os.environ.get('DB_HOST')
    CHANNEL_ID: int = os.environ.get('DB_PORT')


class Settings(BaseSettings):
    bot: BOT_SETTINGS = BOT_SETTINGS()


settings = Settings()
