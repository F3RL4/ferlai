from flask import Flask, render_template, request, jsonify, send_file
import os
import openai
import webbrowser
from tkinter import simpledialog
import tkinter as tk

app = Flask(__name__, static_url_path='/static')

def obter_chave_api():
    """Obtém a chave de API da OpenAI da variável de ambiente."""
    chave = os.getenv("OPENAI_API_KEY")
    if chave is None:
        raise ValueError("A chave de API da OpenAI não foi encontrada. Configure a variável de ambiente OPENAI_API_KEY.")
    return chave

def configurar_chave_api(chave):
    """Configura a chave de API da OpenAI."""
    openai.api_key = chave

def solicitar_prompt():
    """Solicita que o usuário forneça um prompt usando uma caixa de diálogo."""
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    prompt = simpledialog.askstring("Solicitar Prompt", "O que você quer que eu desenhe?")
    return prompt

def gerar_imagem(prompt, num_imagens=1, tamanho="1024x1024"):
    """Gera uma imagem com base no prompt fornecido."""
    resultado = openai.Image.create(
        prompt=prompt,
        n=num_imagens,
        size=tamanho
    )
    return resultado['data'][0]['url']

def abrir_link_no_navegador(url):
    """Abre o link automaticamente no navegador."""
    webbrowser.open(url, new=2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/imagem.html')
def imagem():
    return render_template('imagem.html')

@app.route('/processar', methods=['POST'])
def processar():
    chave_api = obter_chave_api()
    configurar_chave_api(chave_api)

    prompt_usuario = request.form['pergunta']

    if prompt_usuario:
        url_imagem = gerar_imagem(prompt_usuario)

        # Não abra o link automaticamente, apenas retorne a URL
        return jsonify(resposta="Imagem gerada!", url_imagem=url_imagem)

if __name__ == "__main__":
    app.run(debug=True)
