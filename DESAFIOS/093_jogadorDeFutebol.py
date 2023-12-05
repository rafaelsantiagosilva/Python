print(f'{'Exercício 93':-^50}')
# var
jogador = dict()
jogador["Nome"] = str(input('Digite o nome do jogador: '))
jogador["Partidas"] = int(input('\nQuantas partidas ele jogou?\nR:'))
jogador["Gols"] = list()
jogador['Total de Gols'] = 0

# Lendo gols
for i in range(0, jogador['Partidas']):
     jogador['Gols'].append(int(input(f'\nQuantos gols ele fez na {i+1}ºpartida?\nR:')))
     jogador['Total de Gols'] += jogador['Gols'][i]

#Saída 01
print('\n-Informações digitadas-')
for k, v in jogador.items():
     print(f'{k}: {v}')

# Saída 02
print(f'\n{'Resultado':-^50}')
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas, em que fez:')
for i in range(0, len(jogador['Gols'])):
     print(f'-> Na {i+1}ºpartida: {jogador["Gols"][i]} gols')
print(f'{'':-^50}')
print(f'TOTAL: {jogador["Total de Gols"]} gols')
print(f'{'':-^50}')