import os
import openai
import webbrowser
from tkinter import simpledialog
import tkinter as tk  # Adicionando a importação de tkinter

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

def main():
    """Função principal para executar o script."""
    chave_api = obter_chave_api()
    configurar_chave_api(chave_api)

    prompt_usuario = solicitar_prompt()

    if prompt_usuario:
        url_imagem = gerar_imagem(prompt_usuario)

        # Abra o link automaticamente no navegador
        abrir_link_no_navegador(url_imagem)

if __name__ == "__main__":
    main()
