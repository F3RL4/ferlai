import openai
import os

chave = os.getenv("OPENAI_API_KEY")

imagem_url = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-z0TQu3wcrWfDHPgaBxvsqPy1/user-u6KYJPSW7m18DAzo3kPu14Pj/img-MJysuQaipXgROF20yEueLHK5.png?st=2023-12-26T18%3A26%3A16Z&se=2023-12-26T20%3A26%3A16Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-12-25T21%3A42%3A32Z&ske=2023-12-26T21%3A42%3A32Z&sks=b&skv=2021-08-06&sig=wTPEc6s%2Bb8kAFiEcF%2Bmx2OyEWGVxzN3AHrhVcZCkSSE%3D"

# Inicialize o cliente OpenAI para gpt-3.5-turbo
client = openai.Completion.create(
    engine="text-davinci-003",
    prompt=f"Descreva a imagem a seguir:\n{imagem_url}",
    max_tokens=300
)

# Obtenha a resposta do modelo
resposta = client['choices'][0]['text']

# Imprima a resposta
print(resposta)