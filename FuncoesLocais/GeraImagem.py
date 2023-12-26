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

    # Defina o prompt e gere a imagem
    ordem = 'Desenhe um foguete viajando para a Lua'
    resultado = openai.Image.create(
        prompt=ordem,
        n=2,
        size="1024x1024"
    )

    # Obtenha a URL da imagem gerada
    resultado_final = resultado['data'][0]['url']

    # Imprima a URL
    print(resultado_final)
