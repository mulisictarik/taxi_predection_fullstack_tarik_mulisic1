import pandas as pd
import json
from pydantic import BaseModel

from src.taxipred.utils.constants import CLEAN_CSV_PATH

class TaxiData:
    def __init__(self):
        self.df = pd.read_csv(CLEAN_CSV_PATH)


    def to_json(self):
        return json.loads(self.df.to_json(orient="records"))
