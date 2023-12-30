print(f'{'Exercício 95':-^70}')
# var
jogador = dict()
jogadores = list()
opc = 'S'

while opc == 'S':
     #Entrada
     jogador["Nome"] = str(input('\nDigite o nome do jogador: '))
     jogador["Partidas"] = int(input('\nQuantas partidas ele jogou?\nR:'))
     jogador["Gols"] = list()
     jogador['Total de Gols'] = 0
     for i in range(0, jogador['Partidas']):
          jogador['Gols'].append(int(input(f'\nQuantos gols ele fez na {i+1}ºpartida?\nR:')))
          jogador['Total de Gols'] += jogador['Gols'][i]
     jogadores.append(jogador.copy())
     opc = str(input('\nDeseja continuar? [S/N]\nR:')).upper()

# Saída
print(f'{'':=^70}\n{'TABELA':^70}\n{'':=^70}')
print(f'Nome{' '*15}Partidas{' '*10}Gols{' '*10}Total de gols')
for i in range(0, len(jogadores)):
     print(f'{'':-^65}')
     print(f'{jogadores[i]['Nome']}{' '*15}{jogadores[i]['Partidas']}', end='')
     print(f'{' '*10}{jogadores[i]['Gols']}{' '*10}{jogadores[i]['Total de Gols']}')