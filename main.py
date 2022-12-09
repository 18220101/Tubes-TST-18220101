import uvicorn
from fastapi import FastAPI, Request
from dotenv import load_dotenv
from routes.accounts import account_rounter
from routes.insurance import insurance_router
from utils import authorize

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)

load_dotenv()

app = FastAPI()

app.include_router(account_rounter, prefix="/account")
app.include_router(insurance_router, prefix="/insurance")

@app.get("/") 
def home(request: Request):
   authorize(request)
   return { "message":"Welcome to Insurace Fare Prediction API" }