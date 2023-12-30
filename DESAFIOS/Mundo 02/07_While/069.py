print(f'{"Exercício 69":-^50}')
idade = mais_18anos = qtd_homens = qtd_mulheres_menos_20anos = 0
opc = sexo = ''
while True:
    print('\n{:-^45}\n{:^45}\n{:-^45}'.format('', 'CADASTRE UMA PESSOA', ''))
    idade = int(input('Idade: '))
    if idade > 18:
        mais_18anos+=1
    sexo = input('Sexo [M/F]: ').upper()
    if sexo == 'M':
        qtd_homens+=1
    if sexo == 'F' and idade < 20:
        qtd_mulheres_menos_20anos+=1
    print('{:-^45}'.format(''))
    opc = input('\nQuer continuar?[S/N]\nR:').upper()
    if opc != 'S':
        break
print('\n{:-^50}'.format('INFORMAÇÕES'))
print('\nHá {} pessoas maiores de idade;\nHá {} homens;\nHá {} mulheres com menos de 20 anos.'.format(mais_18anos, qtd_homens, qtd_mulheres_menos_20anos))