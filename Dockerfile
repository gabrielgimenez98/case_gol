# Use uma imagem base Python, escolha uma versão adequada
FROM python:3.9-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo de requisitos para o contêiner
COPY requirements.txt .

# Instale as dependências
RUN pip install -r requirements.txt

# Copie o restante do código da sua aplicação para o contêiner
COPY . .

# Exponha a porta em que sua aplicação Flask está ouvindo
EXPOSE 5000

# Comando para iniciar a aplicação Flask
CMD ["python", "app.py"]
