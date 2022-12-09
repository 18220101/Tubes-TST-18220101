def insuranceEntity(item) -> dict:
    return {
            "_id":str(item["_id"]),
            "id":item["id"],
            "name":item["name"],
            "age":item["age"],
            "sex":item["sex"],
            "bmi":item["bmi"],
            "children":item["children"],
            "smoker":item["smoker"],
            "region":item["region"]
    }

def insurancesEntity(entity) -> list:
    return [insuranceEntity(item) for item in entity]