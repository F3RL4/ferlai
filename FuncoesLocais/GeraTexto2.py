import openai
import os

def obter_chave_api():
    """Obtém a chave de API da OpenAI da variável de ambiente."""
    chave = os.getenv("OPENAI_API_KEY")
    if chave is None:
        raise ValueError("A chave de API da OpenAI não foi encontrada. Configure a variável de ambiente OPENAI_API_KEY.")
    return chave

def fazer_pergunta():
    """Solicita uma pergunta ao usuário."""
    print(">>>> F3RL4i <<<<")
    return input("O que você quer saber? \n ")

def gerar_resposta(pergunta, max_tokens=2000, temperature=0.5):
    """Gera uma resposta com base na pergunta usando a API da OpenAI."""
    solicitacao = f"Pergunta: {pergunta}\nResposta:"
    resultado = openai.Completion.create(
        engine="text-davinci-003",
        prompt=solicitacao,
        max_tokens=max_tokens,
        temperature=temperature
    )

    resposta_gerada = resultado['choices'][0]['text']
    # Obtenha o número de tokens usados na resposta
    tokens_usados = resultado['usage']['total_tokens']
    return resposta_gerada, tokens_usados

def main():
    """Função principal para executar o script."""
    chave_api = obter_chave_api()
    openai.api_key = chave_api

    pergunta_usuario = fazer_pergunta()
    resposta, tokens_usados = gerar_resposta(pergunta_usuario)

    print(f"Resposta: {resposta}")
    print(f"Número de Tokens Usados: {tokens_usados}")

if __name__ == "__main__":
    main()
