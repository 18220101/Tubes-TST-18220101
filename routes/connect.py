import requests

def get_bearer_token():
    url = 'https://tubesapi.azurewebsites.net/login'
    data = {"email": "grat@123.com", "password": "hehe"}
    response = requests.post(url, data=data)
    jsonresponse = response.json()
    bearertoken = str(jsonresponse['access_token'])
    return bearertoken

def format_get(url: str):
    link = url
    headers = {"Authorization": f'Bearer {get_bearer_token()}'}
    response = requests.get(link, headers=headers)
    jsonresponse = response.json()
    return jsonresponse

def get_db():
    url = f'https://tubesapi.azurewebsites.net/Prediction/get_prediction_prediction__post'
    return format_get(url)