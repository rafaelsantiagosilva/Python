# AULA 06.5 - VERIFICANDO O TIPO
'''
n = float(input("Escreva um número: "))
print(type(n))

print("É string? ", type(n)==str)
print("É inteiro? ", type(n)==int)
print("É flutuante? ", type(n)==float)

algo = input("Digite algo: ")
print("É numérico? ", algo.isnumeric())
print("É alfabético? ", algo.isalpha())
print("É alfanumérico? ", algo.isalnum())
'''

frase = input("Digite uma frase: ")
print("Ela está somente em maiúscula? ", frase.isupper())
# Existem inúmeras funções para testar o tipo