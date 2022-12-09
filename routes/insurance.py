from typing import List
from database.connection import client
from fastapi import APIRouter, Body, HTTPException, status
from models.insurance import insurance
from schemas.insurance import insuranceEntity, insurancesEntity
from machine_learning.model import insurance_model
from bson import ObjectId
import numpy as np

insurance_router = APIRouter(
    tags=["Prediction"]
)

@insurance_router.get("/", response_model=List[insurance])
async def retrieve_all_insurance() -> List[insurance]:
    return insurancesEntity(client.insurance.insurance.find())

@insurance_router.get("/{id}")
async def retrieve_id_insurace(id: int) -> insurance:
    return insuranceEntity(client.insurance.insurance.find_one({"id":id}))

@insurance_router.get("/new")
async def add_insurance(body: insurance = Body(...)) -> dict:
    client.insurance.insurance.insert_one(dict(body))
    return {
        "message": "Insurance data added"
    }

@insurance_router.post("/insurance_prediction")
async def predict_insurance(body: insurance = Body(...)) -> dict:
    return insurancesEntity(client.insurance.insurance.find())