import requests
import json

# endereço do servidor onde está a API
base_url = "https://economia.awesomeapi.com.br/last/"
info = "USD-BRL"

url = f"{base_url}{info}"

print(url)
# gerar a requisiçãobject
received = requests.get(url)
print('-------------')
print(received)
print("-------------")

print(received.content)
print("--------------")
# Transformando em json ---------------
dado = json.loads(received.content)

print(dado)
print("---------------")
print(f"Nome da moeda: {dado['USDBRL']['name']}\
      \nMaior valor: R$ {dado['USDBRL']['high']}\
      \nMenor valor: R$ {dado['USDBRL']['low']}")