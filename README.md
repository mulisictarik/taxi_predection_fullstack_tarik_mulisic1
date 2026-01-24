# Taxi Price Predictor

Machine learning system for predicting taxi prices based on distance, time, weather, and other factors.

## Setup

1. Install dependencies:

pip install -r requirements.txt

### Run the PPI

python -m uvicorn taxipred.backend.api:app --reload --app-dir src

API runs on `http://localhost:8000`

### Run the frontend

streamlit run src/taxipred/frontend/app.py

Frontend runs on `http://localhost:8501`

## Project structure

- `model_development/` - Jupyter notebooks for data exploration and model training
- `backend/` - FastAPI server with prediction endpoint
- `frontend/` - Streamlit web app for user interface
- `data/` - Dataset and trained model files
- `utils/` - Configuration and constants

## How It Works

1. **Data Preparation** - Cleaned and explored taxi dataset
2. **Model Training** - Trained Random Forest model on historical prices
3. **API** - Serves predictions via REST endpoint
4. **Web UI** - User-friendly interface to get price predictions

<img width="1481" height="787" alt="Skärmbild 2026-01-24 162023" src="https://github.com/user-attachments/assets/4f8dd3a8-c513-4c00-89e4-98a9c2cf12a9" />

