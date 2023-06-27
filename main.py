from flask import Flask, render_template, request
import random
import string
import pandas as pd

app = Flask(__name__)

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def salvar_senha(nome_local, senha):
    df = pd.DataFrame({'Local': [nome_local], 'Senha': [senha]})
    df.to_csv('senhas.csv', mode='a', index=False, header=not pd.read_csv('senhas.csv').empty)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar', methods=['POST'])
def gerar():
    nome_local = request.form['local']
    tamanho_senha = int(request.form['tamanho'])
    
    senha = gerar_senha(tamanho_senha)
    salvar_senha(nome_local, senha)
    
    return render_template('resultado.html', nome_local=nome_local, senha=senha)

if __name__ == '__main__':
    app.run()
