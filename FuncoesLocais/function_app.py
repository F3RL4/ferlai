import azure.functions as func
import logging
import openai
import os  # Importe o módulo 'os' para acessar variáveis de ambiente

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# Recupere a chave da API OpenAI de uma variável de ambiente
chave = os.environ.get('OPENAI_API_KEY')
# "model":"text-davinci-003", "prompt":"qual a velocidade da luz?", "max_tokens":200, "temperature":0}

@app.route(route="FERLAi")
def FERLAi(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Verifique se a chave da API OpenAI está presente
    if not chave:
        return func.HttpResponse("A chave da API OpenAI não está configurada.", status_code=500)

    # Configure a chave da API OpenAI
    openai.api_key = chave

    try:
        req_body = req.get_json()

        # Chamada à OpenAI
        resultado = openai.Completion.create(
            model=req_body['model'],
            prompt=req_body['prompt'],
            max_tokens=req_body['max_tokens'],
            temperature=req_body['temperature']
        )

        # Mostrar a resposta
        resultado_final = resultado['choices'][0]['text']

        return func.HttpResponse(
            f"F3RL4i - {resultado_final}",
            status_code=200
        )
    except Exception as e:
        return func.HttpResponse(f"Erro: {str(e)}", status_code=500)
