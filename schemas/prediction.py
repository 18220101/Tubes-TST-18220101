def predictEntity(item) -> dict:
    return{
        "age": item["age"],
        "sex": item["sex"],
        "bmi": item["bmi"],
        "childern": item["children"],
        "smoker": item["smoker"],
        "region": item["region"]
    }

def predictsEntity(entity) -> list:
    return [predictEntity(item) for item in entity]