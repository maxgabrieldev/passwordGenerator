from flask import Flask, render_template, request  # Importa o Flask
import random  # Importa o módulo random
import string # Importa o módulo string
import pandas as pd # Importa o módulo pandas

app = Flask(__name__) # Instancia o Flask

def gerar_senha(tamanho): # Função para gerar a senha
    caracteres = string.ascii_letters + string.digits + string.punctuation  # Define os caracteres que serão usados na senha
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho)) # Gera a senha
    return senha    # Retorna a senha

def salvar_senha(nome_local, senha): # Função para salvar a senha
    df = pd.DataFrame({'Local': [nome_local], 'Senha': [senha]}) # Cria um DataFrame com o local e a senha
    df.to_csv('senhas.csv', mode='a', index=False, header=not pd.read_csv('senhas.csv').empty) # Salva o DataFrame no arquivo CSV

@app.route('/') # Define a rota da página inicial
def index(): # Função para renderizar a página inicial
    return render_template('index.html') # Renderiza a página inicial

@app.route('/gerar', methods=['POST']) # Define a rota da página de geração de senha
def gerar(): # Função para renderizar a página de geração de senha
    nome_local = request.form['local'] # Pega o nome do local
    tamanho_senha = int(request.form['tamanho']) # Pega o tamanho da senha
    
    senha = gerar_senha(tamanho_senha) # Gera a senha
    salvar_senha(nome_local, senha) # Salva a senha
    
    return render_template('resultado.html', nome_local=nome_local, senha=senha) # Renderiza a página de resultado

if __name__ == '__main__': # Verifica se o arquivo está sendo executado diretamente
    app.run() # Executa o Flask
