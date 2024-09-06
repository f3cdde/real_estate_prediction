import joblib
import numpy as np
import pandas as pd

class PredictionService:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)
        self.columns = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 
                        'population', 'households', 'median_income', 'ocean_proximity_<1H OCEAN', 
                        'ocean_proximity_INLAND', 'ocean_proximity_ISLAND', 'ocean_proximity_NEAR BAY', 
                        'ocean_proximity_NEAR OCEAN']

    def predict(self, features):
        # Criar um DataFrame com os recursos fornecidos
        input_data = pd.DataFrame([features], columns=self.columns)
        
        # Preencher colunas ausentes com zeros
        input_data = input_data.reindex(columns=self.columns, fill_value=0)
        
        prediction = self.model.predict(input_data)
        return prediction[0]

if __name__ == "__main__":
    service = PredictionService("model.joblib")
    features = [8.3252, 41, 6.984127, 1.02381, 322, 2.555556, 37.88, -122.23, 0, 0, 0, 0, 1]
    prediction = service.predict(features)
    print(f"Predicted House Value: {prediction}")
