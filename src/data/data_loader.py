import pandas as pd
import os

class DataLoader:
    def __init__(self, url):
        self.url = url

    def load_data(self):
        try:
            data = pd.read_csv(self.url)
            return data
        except Exception as e:
            raise Exception(f"Erro ao carregar os dados: {e}")

if __name__ == "__main__":
    data_loader = DataLoader(os.getenv("DATA_URL"))
    data = data_loader.load_data()
    print(data.head())
