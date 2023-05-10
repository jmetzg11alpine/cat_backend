from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


# deployment info
# https://www.youtube.com/watch?v=h5wLuVDr0oc

from app.model.model import model
# from model.model import model

from app.helpers import get_filtered_data
# from helpers import get_filtered_data


app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def root():
    return {'message': 'make predictions through the predictor'}

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

class Times(BaseModel):
    startDate: str
    endDate: str

@app.post('/data')
def get_data(times: Times):
    times_dict = times.dict()
    data = get_filtered_data(times_dict['startDate'], times_dict['endDate'])
    return data


