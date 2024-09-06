# Use uma imagem base oficial do Python
FROM python:3.8-slim

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt ./

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código do projeto para o diretório de trabalho
COPY . .

# Defina o PYTHONPATH
ENV PYTHONPATH=/app

# Defina a variável de ambiente DATA_URL
ENV DATA_URL=https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv

# Treine e salve o modelo
RUN python src/models/model.py

# Exponha a porta 5000
EXPOSE 5000

# Comando para iniciar o servidor
CMD ["gunicorn", "-b", "0.0.0.0:5000", "src.app:app"]
