from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
from src.taxipred.utils.constants import MODEL_PATH, SCALER_PATH
from src.taxipred.backend.data_processing import TaxiInput, TaxiData, PredictionOutput

app = FastAPI(title="Taxi Price Predictor", version="1.0")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
model = joblib.load(MODEL_PATH)
preprocessor = joblib.load(SCALER_PATH)
taxi_data = TaxiData()

@app.get("/")
def read_root():
    return {"message": "Taxi Price Predictor API"}

@app.get("/taxi/data")
async def get_taxi_data():
    return taxi_data.to_json()


@app.post("/predict", response_model=PredictionOutput)
async def predict_price(payload: TaxiInput):
    
    # Convert input to DataFrame
    data_df = payload.to_dataframe()
    
    # Transform using preprocessor
    data_preprocessed = preprocessor.transform(data_df)
    
    # Predict
    prediction = model.predict(data_preprocessed)
    
    return {
        "predicted_price": round(float(prediction[0]), 2)
    }