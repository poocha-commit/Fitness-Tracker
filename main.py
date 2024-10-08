import requests,os


API_ID = os.environ['API_ID']

API_KEY=os.environ["API_KEY"]

SHEETY_ENDPOINT=os.environ["SHEETY_ENDPOINT"]

BEARER_TOKEN=os.environ["BEARER_TOKEN"]
print(API_ID,API_KEY)
GENDER = "female"
WEIGHT_KG = 66
HEIGHT_CM = 163
AGE = 19


HOST_DOMAIN="https://trackapi.nutritionix.com"

exercise_endpoint=f"{HOST_DOMAIN}/v2/natural/exercise"


exercise=input("Tell me which exercises you did: ")

headers={
    "x-app-id":API_ID,
    "x-app-key":API_KEY,
}
exercise_params={
    "query":exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE

}
auth_header={
    "Authorization":f'Bearer {BEARER_TOKEN}'
}
response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
result = response.json()
# print(result)


from datetime import datetime
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs,headers=auth_header)

    print(sheet_response.text)