from pathlib import Path

DATA_PATH = Path(__file__).parent.parent /"data"


TAXI_CSV_PATH = DATA_PATH / "taxi_trip_pricing.csv"

MODEL_PATH = DATA_PATH / "taxi_trip_model.joblib"

SCALER_PATH = DATA_PATH / "taxi_scaler.joblib"

CLEAN_CSV_PATH = DATA_PATH / "cleaned_taxi_trip_pricing.csv"
