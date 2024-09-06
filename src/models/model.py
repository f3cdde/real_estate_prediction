from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
import joblib
import os
import pandas as pd
from src.data.data_loader import DataLoader

class Model:
    def __init__(self, data):
        self.data = data
        self.model = RandomForestRegressor()
        self.encoder = OneHotEncoder()
        self.imputer = SimpleImputer(strategy='mean')

    def preprocess_data(self):
        # Separar as variáveis independentes (X) e a variável dependente (y)
        X = self.data.drop("median_house_value", axis=1)
        y = self.data["median_house_value"]

        # Converter variáveis categóricas em variáveis numéricas
        X = pd.get_dummies(X, columns=["ocean_proximity"])

        # Imputar valores ausentes
        X = self.imputer.fit_transform(X)

        # Dividir os dados em conjuntos de treino e teste
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        return X_train, X_test, y_train, y_test

    def train(self):
        X_train, X_test, y_train, y_test = self.preprocess_data()
        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        print(f"Mean Squared Error: {mse}")
        joblib.dump(self.model, "model.joblib")

if __name__ == "__main__":
    data_loader = DataLoader(os.getenv("DATA_URL"))
    data = data_loader.load_data()
    model = Model(data)
    model.train()
