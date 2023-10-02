# Case Gol

Esta é uma aplicação Flask que permite aos usuários autenticados selecionar um mercado e um intervalo de datas para visualizar um gráfico do RPK (Revenue Passenger Kilometers) ao longo do tempo. A aplicação inclui autenticação de usuário, filtros para seleção de mercado e intervalo de datas, e a visualização de gráficos.

## Pré-requisitos

Antes de começar, certifique-se de que você tenha o seguinte software instalado em seu ambiente:

- Python 3.x
- Flask
- Redis (para autenticação de usuário)
- MySQL ou SQLite (para armazenar dados)

## Instalação

1. **Clonando o repositório**

   Clone este repositório para o seu ambiente local:

   ```
   git clone https://github.com/gabrielgimenez98/case_gol.git
   cd case_gol

2. **Criando Ambiente Virtual**

   Clone este repositório para o seu ambiente local:

   ```
    python3 -m venv venv
    source venv/bin/activate  # No Windows, use "venv\Scripts\activate"

3. **Instalando dependências**

   Instale as dependências usando

   ```
    pip install -r requirements.txt
    
4. **Rodando o projeto localmente**

   ```
    flask run

