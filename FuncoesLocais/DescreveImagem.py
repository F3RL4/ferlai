import openai
import os
import base64
import requests
from tkinter import Tk, filedialog

# Chave da API OpenAI
api_key = os.getenv("OPENAI_API_KEY")

# Função para codificar a imagem
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Abrir o diálogo de arquivo para escolher uma imagem
root = Tk()
root.withdraw()  # Ocultar a janela principal
image_path = filedialog.askopenfilename(title="Escolha uma imagem", filetypes=[("Imagens", "*.png;*.jpg;*.jpeg")])
root.destroy()  # Fechar a janela Tkinter após o diálogo de arquivo ser fechado

# Verificar se o usuário selecionou uma imagem
if not image_path:
    print("Nenhuma imagem selecionada.")
else:
    # Obter a string base64
    base64_image = encode_image(image_path)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "O que há nesta imagem?"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    print(response.json())
