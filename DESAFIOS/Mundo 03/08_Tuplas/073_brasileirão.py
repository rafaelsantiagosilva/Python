times = ('Flamengo', 'Palmeiras', 'Athletico Paranaense', 'Atlético Mineiro', 'São Paulo', 'Fluminense', 'Fortaleza', 'Corinthians', 'Santos', 'Internacional', 'Grêmio', 'América Mineiro', 'Atlético Goianiense', 'Ceará', 'Bahia', 'Botafogo', 'Red Bull Bragantino', 'Cruzeiro', 'Goiás', 'Cuiabá')
print(f'{"Exercício 73":-^50}')
print(f'\n{"Primeiros 5 colocados:":-^45}')
for nome in range(0, 5):
    print(f'{nome+1}º: {times[nome]}')
print(f'\n{"Últimos 4 colocados:":-^45}')
for nome in range(len(times)-1, 15, -1):
    print(f'{nome+1}º: {times[nome]}')
print(f'\n{"Ordem alfabética dos 20 primeiros times:":-^45}')
times = sorted(times)
for nome in times:
    print(nome)
print(f'\n{"Posição da Chapecoense entre os 20 colocados:":-^50}')
print(times.index('Chapecoense'))
