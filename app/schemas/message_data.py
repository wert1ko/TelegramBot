from pydantic import BaseModel, EmailStr


class MessageData(BaseModel):
    full_name: str
    email: EmailStr
    phone_number: str
    type_of_activity: str
