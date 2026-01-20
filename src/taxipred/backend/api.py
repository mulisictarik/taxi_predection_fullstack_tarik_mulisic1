from fastapi import FastAPI
import joblib
import pandas as pd 
from pathlib import Path
from taxipred.backend.data_processing import TaxiData

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "model_development" / "taxi_trip_model.joblib"
SCALER_PATH = BASE_DIR / "model_development" / "taxi_scaler.joblib"

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
taxi_data = TaxiData()

@app.get("/")
def read_root():
    return {"message": "API is online"}

@app.get("/taxi/")
async def read_taxi_data():
    return taxi_data.to_json()

@app.post("/predict")
async def predict_price(data: dict):
    input_list = data["features"]

    df = pd.DataFrame([input_list])

    scaled_data = scaler.transform(df)

    prediction = model.predict(scaled_data)

    return {"estimated_price": round(float(prediction[0]),2)}