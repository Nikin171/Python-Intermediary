# OBS: O ARQUIVO TXT TEM QUE ESTAR NO MESMO DIRETÓRIO.

# with open(f"teste.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     arquivo.write("O que vou escrever")

#     print(conteudo)

# try:
#     arquivo = open(f"teste.txt", "r")
#     conteudo2 = arquivo.read()
# finally:
#     arquivo.close()
#     print(conteudo)
'''
try:
    arquivo = open(f"teste.txt", "w")
    arquivo.write("O que vou escrever")
finally:
    arquivo.close()

with open(f"teste.txt", "r") as arquivo:
    conteudo = arquivo.read()

print(conteudo)
'''
def verificar_adicionar_conteudo(arquivo, conteudo):

    with open('teste.txt', 'r') as arquivo:
        if conteudo in arquivo.read():
            print("O conteúdo já está no arquivo.")
            return

    with open('teste.txt', 'a') as arquivo:
        arquivo.write(conteudo + '\n')
        print("Conteúdo adicionado seu boca de sacola.")

nome_arquivo = 'teste.txt'
novo_conteudo = 'O que vai adicionar'

verificar_adicionar_conteudo(nome_arquivo, novo_conteudo)



#'r' = ready >>> Leitura dos dados existentes no conteudo.
#'w' = write >>> Ele apaga tudo e cria do 0.
#'a' = append >>> Ele anexa, continua escrever com o que ja existia.