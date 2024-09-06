from flask import Blueprint, request, jsonify
from src.services.prediction_service import PredictionService

app = Blueprint('prediction_app', __name__)
service = PredictionService("model.joblib")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        features = data["features"]
        # Adicionar colunas de variáveis categóricas codificadas
        features.extend([0, 0, 0, 0, 1])
        prediction = service.predict(features)
        return jsonify({"prediction": prediction})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
