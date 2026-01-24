import pandas as pd
import json
from pydantic import BaseModel, Field
from typing import Literal
from src.taxipred.utils.constants import CLEAN_CSV_PATH


class TaxiInput(BaseModel):
    """User input for taxi price prediction"""
    trip_distance: float = Field(ge=1.0, le=70.0, description="Distance in km")
    time_of_day: Literal["Morning", "Afternoon", "Evening", "Night"] = Field(description="Time of day")
    day_of_week: Literal["Weekend", "Weekday"] = Field(description="Weekend or Weekday")
    passenger_count: int = Field(ge=1, le=4, description="Number of passengers")
    traffic_conditions: Literal["Low", "Medium", "High"] = Field(description="Traffic level")
    weather: Literal["Clear", "Snow", "Rain"] = Field(description="Weather condition")
    
    def to_dataframe(self):
        """Convert to DataFrame for preprocessing"""
        return pd.DataFrame({
            'Trip_Distance_km': [self.trip_distance],
            'Time_of_Day': [self.time_of_day],
            'Day_of_Week': [self.day_of_week],
            'Passenger_Count': [self.passenger_count],
            'Traffic_Conditions': [self.traffic_conditions],
            'Weather': [self.weather]
        })


class TaxiData:
    def __init__(self):
        self.df = pd.read_csv(CLEAN_CSV_PATH)

    def to_json(self):
        return json.loads(self.df.to_json(orient="records"))


class PredictionOutput(BaseModel):
    predicted_price: float = Field(description="Predicted taxi price") 