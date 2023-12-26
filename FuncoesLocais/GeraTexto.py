import openai
import os

# Recupere a chave de API de uma variável de ambiente
chave = os.getenv("OPENAI_API_KEY")

# Verifique se a chave de API está presente
if chave is None:
    print("A chave de API da OpenAI não foi encontrada. Configure a variável de ambiente OPENAI_API_KEY.")
else:
    # Configure a chave de API
    openai.api_key = chave

    # Solicite que o usuário faça uma pergunta
    print(">>>> F3RL4i <<<<")
    pergunta_usuario = input("O que você quer saber? \n ")

    # Crie uma solicitação para a IA responder à pergunta
    solicitacao = f"Pergunta: {pergunta_usuario}\nResposta:"

    # Gere a resposta com base na solicitação
    resultado = openai.Completion.create(
        engine="text-davinci-003",
        prompt=solicitacao,
        max_tokens=150,
        temperature=0
    )

    # Obtenha a resposta gerada
    resposta_gerada = resultado['choices'][0]['text']

    # Imprima a resposta
    print(f"Resposta: {resposta_gerada}")
