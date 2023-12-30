print(f'{"Exercício 72":-^50}')
n_extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    n = int(input('\nDigite um número [0-20]: \nR:'))
    if n >= 0 and n <= 20:
        break
print(f'Você digitou "{n_extenso[n]}"')