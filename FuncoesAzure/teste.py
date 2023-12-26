from openai import OpenAI
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="a white siamese cat",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url


import os
import openai

# Recupere a chave de API de uma variável de ambiente
chave = os.getenv("OPENAI_API_KEY")

# Verifique se a chave de API está presente
if chave is None:
    print("A chave de API da OpenAI não foi encontrada. Configure a variável de ambiente OPENAI_API_KEY.")
else:
    # Configure a chave de API
    openai.api_key = chave


    ##########################


      # Solicite que o usuário forneça um prompt
    print(">>>> F3RL4i <<<<")
    #ordem = input("O que você quer que eu desenhe?\n ")

#client = openai()
    # Defina o prompt e gere a imagem
    #ordem = 'Desenhe um foguete viajando para a Lua'

client = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Você é um bot que fala sobre imagens."},
        {"role": "user", "content": "Descreva a imagem a seguir:"},
        {"role": "assistant", "content": f"https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"},
    ]
)

resultado = openai.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
             "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)
    # Imprima a URL
print(resultado.choices[0])