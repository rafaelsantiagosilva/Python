# Básico dos dicionários
pessoas = {
     'Nome': "Gustavo",
     "Sexo": "M",
     "Idade": 22
};

print('\nImprimindo: ')
print(f'O {pessoas['Nome']} tem {pessoas["Idade"]} anos');

print("\nImprimindo tudo:");
print(pessoas.values());
print(pessoas.keys());
print(pessoas.items());

print("\nImprimindo bonito:");
for k, v in pessoas.items():
     print(f"{k}: {v}");

print("\nApagando o sexo: ");
del pessoas["Sexo"];
for k, v in pessoas.items():
     print(f"{k}: {v}");

print('\nMudando o nome: ');
pessoas["Nome"] = "Rafael";
for k, v in pessoas.items():
     print(f"{k}: {v}");

print('\nAdicionando o peso: ');
pessoas["Peso"] = 65.78;
for k, v in pessoas.items():
     print(f"{k}: {v}");

# Lendo dicionários
estado = dict();
brasil = list()

for c in range(0, 3):
     estado['UF'] = str(input('\nUnidade Federativa: '));
     estado["Sigla"] = str(input('Sigla do Estado: '));
     brasil.append(estado.copy());

for estados in brasil:
     print("\n");
     for k, v in estados.items():
          print(f'{k}: {v}');

# Organizando
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