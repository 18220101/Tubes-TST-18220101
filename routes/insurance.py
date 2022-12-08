from typing import List
from fastapi import APIRouter, Body, HTTPException, status
from models.insurance import insurance
import pickle
import json

insurance_router = APIRouter(
    tags=["Insurance"]
)

with open("customer.json", "r") as read_file:
    data = json.load(read_file)

insurance_model = pickle.load(open('regressor_model.sav','rb')) 

@insurance_router.post("/")
def insurance_prediction(input_parameters : insurance):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)

    id = input_dictionary['id']
    name = input_dictionary['nama']
    age = input_dictionary['age']
    sex = input_dictionary['sex']
    bmi = input_dictionary['bmi']
    children = input_dictionary['children']
    smoker = input_dictionary['smoker']
    region = input_dictionary['region']

    input_list = [id, name, age, sex, bmi, children, smoker, region]

    prediction = insurance_model.predict([input_list])

    print ('The insurance cost is USD ', prediction[0])
