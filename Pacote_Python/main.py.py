#Faça um pacote, contendo 2 modulos: PESSOA.PY e MAIN.py 
#no modulo PESSOA faça uma funcao que calcule a idade, dado o dia de hoje como nase e o ano de nascimento dela. Essa funcao recebe como parametro somente a data de nascimento e retorna unicamente o valor inteiro da idade
#no modulo MAIN solicite ao usuario seu nome e ano de nascimento, alem disto, solicite tambem o ano em que estamos, chame a funcao CALCULAR_IDADE e imprima o resultado.
'''
import pessoa
import datetime
nome = input("Qual é o seu nome? ")
ano_nascimento = int(input("Em que ano você nasceu? "))
ano_atual = int(input("Em que ano estamos? "))

data_nascimento = datetime.date(ano_nascimento, 1, 1)
idade = pessoa.calcular_idade(data_nascimento)

print(f"Olá, {nome}! Você tem {idade} anos.")

'''

#Vamos melhorar o exercicio anterior, agora ao inves de solicitar o ano em que estamos, utilize a biblioteca que o python disponbiliza
#para pegar este valor. Alem disto, o usuario deve informar, nao somente o ano, mas tambem o dia e mes de aniversario(um em cada entrada diferente)

import pessoa
import datetime
nome = input("Qual é o seu nome? ")

dia_nascimento = int(input(f"Digite o dia de nascimento? "))
mes_nascimento = int(input(f"Digite o mês de nascimento? (Digite apenas números de 1 á 12): "))
ano_nascimento = int(input(f"Digite o ano de nascimento? "))

data_nascimento = datetime.date(ano_nascimento, mes_nascimento, dia_nascimento)
idade = pessoa.calcular_idade(data_nascimento)

print(f"Olá, {nome}! Você tem {idade} anos.")

