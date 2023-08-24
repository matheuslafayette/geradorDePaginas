from senha import API_KEY
import requests
import json

headears = {"Authorization": f"Bearer {API_KEY}", "Content-Type":"application/json"}
link = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo"

body_mensagem = {
    "model": id_modelo,
    "messages": [{"role":"user", "content":"crie 5 frases de efeitos, sendo persuasivos, para vender microondas"}]
}

body_mensagem = json.dumps(body_mensagem)

requisicao = requests.post(link, headears=headears, data=body_mensagem)
reposta = requisicao.json
mensagem = resposta["choices"][0]["message"]["content"]
