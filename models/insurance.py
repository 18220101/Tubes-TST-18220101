from pydantic import BaseModel

class insurance(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    bmi: float
    children: int
    smoker: bool
    region: str