print(f'{"Exercício 67":-^50}')
num = i = 0
while True:
    num = int(input('Digite um número [negativo para parar]: '))
    if num < 0:
        break
    print(f'\n{"TABUADA":-^25}')
    i=0
    while i <= 10:
        print(f'{num} x {i} = {num*i}')
        i+=1
    print(f"{'':-^25}\n")
print('\nTchau Tchau!')