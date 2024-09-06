from flask import Flask
from src.controllers.prediction_controller import app as prediction_app

app = Flask(__name__)

# Registre o blueprint do controlador de previsão
app.register_blueprint(prediction_app, url_prefix='/')

@app.route('/')
def index():
    return "Bem-vindo ao Real Estate Prediction API!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
