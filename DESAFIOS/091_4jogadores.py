from random import randint as rand
from time import sleep as slp
from operator import itemgetter
print(f'{'Exercício 91':-^50}')
jogadores = dict()
for i in range(0, 4):
     jogadores["Jogador "+ str(i+1)] = rand(1, 6)
     print(f'Jogador {i+1}: {jogadores["Jogador "+ str(i+1)]}')
     slp(0.5)
ranking = list()
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(f'{'Ranking':-^50}')
for i, v in enumerate(ranking):
     print(f'{i+1}º: {v[0]} -> {v[1]}')
print(f'{'':-^50}')