import uvicorn
from fastapi import FastAPI, Request
from dotenv import load_dotenv
from pydantic import BaseModel
from routes.accounts import account_rounter
from routes.insurance import insurance_router
from utils import authorize

load_dotenv()

app = FastAPI()

app.include_router(account_rounter, prefix="/login")
app.include_router(insurance_router, prefix="/insurance_prediction")

@app.get("/") 
def identitas(request: Request):
   authorize(request)
   return { "Natasha Tiovanny Silaban (18220101)" }