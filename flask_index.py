from flask import Flask, render_template
app = Flask(__name__)
#Na função, retorne render_template(‘index.html’)
@app.route("/index")
def first_webpage():
    #Crie uma variável
    
    #Passe a variável no modelo
    
app.run(debug=True)
