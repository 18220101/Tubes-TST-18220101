import json
import jwt
from fastapi import APIRouter, HTTPException, status, Response
from utils import get_hash, encode_token, SECRET, authorize
from models.accounts import SignIn

account_rounter = APIRouter(
    tags=["Account"]
)

with open("user.json", "r") as read_file:
    akun = json.load(read_file)

@account_rounter.post("/signin")
def SignIn(param: SignIn, response: Response):
    found = False
    for i in range (len(akun)) :
        if (param.username == akun[i]["username"]):
            found = True
            if (get_hash(param.password) == akun[i]["password"]):
                token = encode_token(param.username)
                print(token)
                return { 
                    "message": "Login berhasil",
                    "data": { "token": token }
                }
            else:
                response.status_code = status.HTTP_400_BAD_REQUEST
                return { "message": "Password salah"}
    if not found:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return { "message": "Akun tidak ditemukan" }
