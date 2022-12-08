from pydantic import BaseModel

class LoginParamater(BaseModel):
    username: str
    password: str