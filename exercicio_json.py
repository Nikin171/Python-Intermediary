#Pegar a funcao de metereologia e cep e fazer uma tupla onde vai ser a junçao das duas coisas

# import requests

# def get_cidade(entrada):
#     cep = ''

#     for caracter in entrada[0]:
#         if caracter in '0123456789':
#             cep += caracter

#     if len(cep) != 8:
#          return 'Cep não é válido!!!'
    
#     viacep_url = (f'https://viacep.com.br/ws/{cep}/json/')
#     metereologia_url = (f'https://goweather.herokuapp.com/weather/{entrada[1]}')

#     resposta_cep = requests.get(viacep_url)
#     resposta_metereologia = requests.get(metereologia_url)

#     return resposta_cep.text, resposta_metereologia.text

# cep = input("Qual o CEP? ")
# cidade = input("Qual a cidade? ")

# logradouro, metereologia = get_cidade((cep, cidade))

# print(logradouro)
# print(metereologia)


import requests
import json

def get_cidade(entrada):
    cep = ''

    for caracter in entrada:
        if caracter in '0123456789':
            cep += caracter

    if len(cep) != 8:
         return 'Cep não é válido!!!'
    
    viacep_url = (f'https://viacep.com.br/ws/{cep}/json/')

    resposta_cep = requests.get(viacep_url)
    resposta_json = json.loads(resposta_cep.text)
    cidade = resposta_json['localidade']

    metereologia_url = (f'https://goweather.herokuapp.com/weather/{cidade}')
    resposta_metereologia = requests.get(metereologia_url)

    return resposta_cep.text, resposta_metereologia.text

cep = input("Qual o CEP? ")

logradouro, metereologia = get_cidade(cep)

print(logradouro)
print(metereologia)
