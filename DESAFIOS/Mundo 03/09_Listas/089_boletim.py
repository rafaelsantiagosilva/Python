print(f'{'Exercício 89':-^50}\n')
# Var
aluno = list()
opc = 0
alunos = list()

# Entrada
qtd_alunos = int(input('Gostaria de armazenar a nota de quantos alunos?\nR:'))
print(f'\n{'-':-^45}')
for i in range(0, qtd_alunos):
     aluno.append(str(input(f'Digite o nome do {i+1}º aluno: ')))
     print(f"Digite a NOTA 1 do {i+1}º aluno: ", end='')
     aluno.append(float(input()))
     print(f"Digite a NOTA 2 do {i+1}º aluno: ", end='')
     aluno.append(float(input()))
     aluno.append((aluno[1] + aluno[2])/2)
     print('\n')
     alunos.append(aluno[:])
     aluno.clear()
print(f'{'B O L E T I M':=^45}')

# Processamento
print(f'Nome{'Nº':^22}{'Média':^44}\n{'=':=^65}')
for i in range(0, len(alunos)):
     print(f'{str(alunos[i][0])}{str(i+1):>10}{str(alunos[i][3]):>30}\n{'-':-^65}')
print(f'{"=":=^65}')

# Saída
while opc != 999:
     opc = int(input("\nDeseja ver as notas de qual aluno? [999 = parar]\nR:"))
     if opc != 999 and opc <= len(alunos) and opc >= 1:
          print(f"\n{alunos[opc-1][0]}: {alunos[opc-1][3]}")