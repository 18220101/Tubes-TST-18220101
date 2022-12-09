from typing import List
from database.connection import client
from fastapi import APIRouter, Body, HTTPException, status
from models.insurance import insurance, insurance_prediction
from schemas.insurance import insuranceEntity, insurancesEntity
from bson import ObjectId
from routes.connect import *
import numpy as np
import pickle

with open('.\models\insurance_prediction.pickle', 'rb') as f:
    insurance_model = pickle.load(f)

#model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), '.\models\insurance_prediction.pickle')
#model = joblib.load(model_path)

insurance_router = APIRouter(
    tags=["Insurance"]
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
async def predict_insurance(body: insurance_prediction):
    input = dict(body)
    input_data = [input['age'], input['sex'], input['bmi'], input['children'], input['smoker'], input['region']]
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = insurance_model.predict(input_data_reshaped)
    return ('The insurance cost is USD ', prediction[0])

@insurance_router.get("/Prediction/get_prediction_prediction__post")
def combining_api():
    return get_db(url)