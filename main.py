from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from catboost import CatBoostRegressor

model = CatBoostRegressor()
model.load_model('cat_model')

weight = 19363
vehicle_size = 'TRACTOR'
billed_miles = 1128
pickup_state = 'TN'
deliver_state = 'TX'
duration_hours = 73

def get_prediction(weight, vehicle_size, billed_miles, pickup_state, deliver_state, duration_hours):
    return model.predict([weight, vehicle_size, billed_miles, pickup_state, deliver_state, duration_hours])


app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Features(BaseModel):
    distance: int
    duration: int
    endLocation: str
    startLocation: str
    vehicleType: str
    weight: int

@app.post('/')
def predict(features: Features):
    f_dict = features.dict()
    prediction = model.predict([f_dict['weight'], f_dict['vehicleType'], f_dict['distance'], f_dict['startLocation'], f_dict['endLocation'], f_dict['duration']])
    rpm = prediction / f_dict['distance']
    return {'predicted_total': round(prediction), 'predicted_rpm': round(rpm,2)}

@app.get('/')
def root():
    return {'message': 'make predictions through the predictor'}

