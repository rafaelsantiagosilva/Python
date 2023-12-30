print('{:-^40}'.format('Exercício 37'))
num = int(input("Digite um número: "))
print('{:-^40}\nVocê deseja converter ele em que base?\n{:-^40}'.format('', ''))
print('Binário [1]')
print('Octal [2]')
print('Hexadecimal [3]')
opc = int(input('Digite uma das opções acima: '))
print('{:-^40}'.format(''))
print('\n{:=^40}\n{:^40}\n{:=^40}'.format('', 'CONVERSÃO', ''))
if opc == 1:
    msg = 'Binário'
    conversao = bin(num)
elif opc == 2:
    msg = 'Octal'
    conversao = oct(num)
elif opc == 3:
    msg = 'Hexadecimal'
    conversao = hex(num)
else:
    msg = 'ERRO'
    conversao = 'Digite somente uma das opções acima!'
print('{}:{}'.format(msg, conversao))
print('{:=^40}'.format(''))