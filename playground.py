import os
API_KEY="57bde74814064e12bfed73f6981dbef9"
API_ID="f5ae7e87"
SHEETY_ENDPOINT="https://api.sheety.co/191a7107a667bcf8510b78362b4e753e/workoutTracking/workouts"
BEARER_TOKEN="dsdsdw334353tfrv5u8j86"


os.environ["API_ID"] = API_ID

os.environ["API_KEY"] = API_KEY

os.environ["SHEETY_ENDPOINT"] = SHEETY_ENDPOINT

os.environ["BEARER_TOKEN"] = BEARER_TOKEN
value=os.environ['API_ID']
print(value)
import pprint 
  
# Get the list of user's 
env_var = os.environ 
  
# Print the list of user's 
print("User's Environment variable:") 
pprint.pprint(dict(env_var), width = 1) 

