# Real Estate Prediction

Este é um projeto avançado de previsão de preços de imóveis utilizando Python, IA e Machine Learning. Utilizamos o banco de dados **Ames Housing Dataset** para treinar um modelo de regressão que prevê o valor mediano das casas.

## Estrutura do Projeto

real-estate-prediction/
│
├── src/
│   ├── data/
│   │   └── data_loader.py
│   ├── models/
│   │   └── model.py
│   ├── services/
│   │   └── prediction_service.py
│   ├── controllers/
│   │   └── prediction_controller.py
│   ├── utils/
│   │   └── logger.py
│   ├── app.py
│   └── config.py
├── notebooks/
│   └── EDA.ipynb
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
├── .gitignore
└── README.md


## Dependências

- pandas
- numpy
- scikit-learn
- flask
- gunicorn
- joblib
- requests

## Configuração do Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis de ambiente:


FLASK_APP=src/app.py FLASK_ENV=development DATA_URL=https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv


## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/real-estate-prediction.git

2. Navegue até o diretório do projeto:
   cd real-estate-prediction

3. Instale as dependências:
   pip install -r requirements.txt

## Executando o Projeto

Usando Docker
1. Construa e inicie os serviços Docker:
   docker-compose up --build

2. Acesse a aplicação no navegador em http://localhost:5000.

Usando Python Localmente
1. Carregue os dados e treine o modelo:
   python src/models/model.py

2. Inicie o servidor Flask:
   flask run

3. Acesse a aplicação no navegador em http://localhost:5000.

## Endpoints da API

Previsão de Preços de Imóveis
 URL: /predict
 Método: POST
 Corpo da Requisição:

JSON
{
  "features": [8.3252, 41, 6.984127, 1.02381, 322, 2.555556, 37.88, -122.23]
}

 Resposta:

JSON
{
  "prediction": 452600.0
}

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.


### Passos para Garantir que o Projeto está Funcional

1. **Clone o repositório**: Certifique-se de que você pode clonar o repositório do GitHub.
2. **Crie os arquivos necessários**: Certifique-se de que todos os arquivos mencionados acima estão presentes e configurados corretamente.
3. **Construa e inicie os serviços Docker**: Construa e inicie os serviços Docker com o comando:

   ```bash
   docker-compose up --build

4. Aguarde até que todos os serviços estejam prontos: Certifique-se de que todos os serviços estejam prontos antes de tentar acessar a aplicação no navegador.
5. Acesse a aplicação no navegador: Acesse a aplicação no navegador em http://localhost:5000.