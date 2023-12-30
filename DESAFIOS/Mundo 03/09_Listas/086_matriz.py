print(f'{"Exercício 86":-^50}')
print(f'\n{"Matriz 3x3":=^45}')
mat = list()
lin = list()
i = j = 0
for i in range(0, 3):
     for j in range(0,3):
          print(f"Digite um número para a posição [{i+1} , {j+1}]: ", end='')
          lin.append(int(input()))
     mat.append(lin[:])
     lin.clear()
print("A matriz digitada foi: \n")
for i in range(0, 3):
     for j in range(0,3):
          print(f'{mat[i][j]} ', end='')
     print('\n')
