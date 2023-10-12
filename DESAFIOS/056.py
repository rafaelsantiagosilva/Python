print('{:-^50}'.format('Exercício 56'))
media_idades = 0
maior_idade_homem = 0
homem_maisvelho = ''
mulheres_menor20anos = 0
for i in range(0, 4):
    nome = str(input('\nDigite o nome da {}º pessoa: '.format(i+1)))
    idade = int(input('Digite a idade da {}º pessoa: '.format(i+1)))
    media_idades+=idade
    sexo = str(input('Digite o sexo[M/F/O] da {}º pessoa: '.format(i+1))).upper()
    if sexo == 'M' and idade > maior_idade_homem:
        homem_maisvelho = nome
    if sexo == 'F' and idade < 20:
        mulheres_menor20anos+=1
media_idades /= 4
print('\n{:-^50}'.format('INFORMAÇÕES'))
print('-> A média de idades é igual a', media_idades)
print('-> O homem mais velho é o', homem_maisvelho)
print('-> Há {} mulheres com menos de 20 anos'.format(mulheres_menor20anos))