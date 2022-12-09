from pydantic import BaseModel
from bson import ObjectId

class insurance(BaseModel):
    _id: ObjectId()
    id: int
    name: str
    age: int
    sex: str
    bmi: float
    children: int
    smoker: bool
    region: str

class insurance_prediction(BaseModel):
    age: int
    sex: int
    bmi: float
    children: int
    smoker: int
    region: int