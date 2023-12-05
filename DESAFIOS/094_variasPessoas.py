from datetime import datetime as dt
print(f'{'Exercício 94':-^50}')

# Var
ano_atual = dt.now().year
pessoas = list()
pessoa = dict()
mulheres = list()
pessoas_idade_acima_media = list()
qtd_pessoas = 0
media_de_idade = 0
opc = 'S'

# Entrada
while opc == 'S':
     pessoa['Nome'] = str(input('Digite o nome de uma pessoa: '))
     pessoa['Sexo'] = str(input('Digite o sexo desta pessoa [M/F]: ')).upper()
     while pessoa['Sexo'] != 'M' and pessoa['Sexo'] != 'F':
          pessoa['Sexo'] = str(input('Por favor, digite somente uma das opções [M/F]: ')).upper()
     pessoa['Ano de nascimento'] = int(input('Digite o ano de nascimento desta pessoa: '))
     pessoa['Idade'] = ano_atual - pessoa['Ano de nascimento']
     pessoas.append(pessoa.copy())

     # Processamento
     qtd_pessoas+=1
     media_de_idade+=pessoa['Idade']
     opc = str(input('\nDeseja continuar? [S/N]\nR:')).upper()
media_de_idade /= qtd_pessoas
for i in pessoas:
     if i['Idade'] > media_de_idade:
          pessoas_idade_acima_media.append(i.copy())
     if i['Sexo'] == 'F':
          mulheres.append(i.copy())

# Saída
print(f'{'Informações':-^50}')
print(f'-> Foram cadastradas {qtd_pessoas} pessoas')
print(f'-> A média de idade é de {media_de_idade} anos')
print(f'-> As mulheres são: ')
for i in range(0, len(mulheres)):
     print(f'  • {mulheres[i]['Nome']}, com {mulheres[i]['Idade']} anos ({mulheres[i]['Ano de nascimento']})')
print(f'-> As pessoas com idade acima da média são: ')
for i in range(0, len(pessoas_idade_acima_media)):
     print(f'  • {pessoas_idade_acima_media[i]['Nome']}, com {pessoas_idade_acima_media[i]['Idade']} anos ({pessoas_idade_acima_media[i]['Ano de nascimento']})')
print(f'{'':-^50}')