#Importando o módulo flask no projeto
from flask import Flask, render_template

#Crie um objeto da classe Flask
app = Flask(__name__)

#A função route() da classe Flask
@app.route("/")

#A URL ‘/’ é ligada à função  first_flask.
def first_flask():

#Defina uma função com um endpoint diferente

@app.route("/flask_2")
def second_flask():

#Na função, retorne render_template(‘index.html’)

@app.route("/index")
def first_webpage():
    #Crie uma variável
    
    # Passe a variável no modelo

#Execute usando o argumento debug
app.run(debug=True)