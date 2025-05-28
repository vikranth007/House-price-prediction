from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

# Load model
model = joblib.load("model.pkl")

app = FastAPI(title="House Price Prediction API")

class HouseFeatures(BaseModel):
    crim: float
    zn: float
    indus: float
    chas: int
    nox: float
    rm: float
    age: float
    dis: float
    rad: int
    tax: float
    ptratio: float
    b: float
    lstat: float

@app.get("/")
def root():
    return {"message": "Welcome to House Price Prediction"}

@app.post("/predict")
def predict_price(features: HouseFeatures):
    input_data = np.array([[features.crim, features.zn, features.indus,
                            features.chas, features.nox, features.rm,
                            features.age, features.dis, features.rad,
                            features.tax, features.ptratio, features.b,
                            features.lstat]])
    prediction = model.predict(input_data)[0]
    return {"predicted_price": round(prediction, 2)}
