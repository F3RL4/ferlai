import openai

chave = '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'
ordem = qual a cor do sol?'

openai.api_key = chave

resultado = openai.Completion.create(
  model="text-davinci-003",
  prompt=ordem,
  max_tokens=100,
  temperature=0
)

resultado_final = resultado['choices'][0]['text']

print(resultado_final)