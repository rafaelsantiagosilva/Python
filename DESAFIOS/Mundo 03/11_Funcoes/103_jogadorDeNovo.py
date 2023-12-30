print(f'{'Exercício 103':-^50}')

def mostrar_info(nome, gols):
     return f'O jogador {nome} fez {gols} gols!'

nome = str(input('Digite o nome do jogador: '))

if nome == '' or nome == ' ':
     nome = "<desconhecido>"

try:
     gols = float(input('Digite a quantidade de gols que ele fez: '))
     gols = int(gols)
except ValueError:
     gols = 0

print(mostrar_info(nome, gols))