# desafio_grafos

# PID

Rede de Grafos

Implementou-se uma API Django conectada a um Banco MySql.
A partir de requisições a essa API os dashboards podem ser acesados e modificados.


# Passos iniciais para executar a aplicação


## 1) Criar ambiente virtual para isolar dependências


*No Windows*:

python -m venv env

*No Linux*:

python3 -m venv env


## 2) ativar ambiente virtual


*No Windows*:

env\scripts\activate

*No Linux*:

source env/bin/activate


## 3) Instalar dependências


*No Windows*:

pip install -r requirements.txt

*No Linux*:

pip3 install -r requirements.txt


## 5) Preparar Banco de dados

*No Windows* ou *No Linux*:

python manage.py makemigrations

python3 manage.py migrate


## 5) subir servidor por padrão na porta 8000

*No Windows*:

python manage.py runserver

*No Linux*:

python3 manage.py runserver

*Caso queira manter aberto em uma porta específica no Linux*

python3 manage.py runserver 10.11.80.77:5000 &
