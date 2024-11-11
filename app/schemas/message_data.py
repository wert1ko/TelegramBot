from pydantic import BaseModel


class MessageData(BaseModel):
    full_name: str
    phone_number: str
    comment:str
