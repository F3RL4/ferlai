chave = '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'
ordem = 'Desenhe um foguete viajando para a Lua'

import openai
openai.api_key = chave

resultado = openai.Image.create(
    prompt=ordem,
    n=2,
    size="1024x1024"
)

resultado_final = resultado['data'][0]['url']

print(resultado_final)