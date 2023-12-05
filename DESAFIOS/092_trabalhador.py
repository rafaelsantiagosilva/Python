from datetime import datetime as date
print(f'{'Exercício 92':-^50}')
ano_atual = date.now().year
trabalhador = dict()

trabalhador["Nome"] = str(input('Digite o nome do trabalhador: '))
trabalhador["Ano de nascimento"] = int(input('Digite o ano de nascimento do funcionário: '))
trabalhador["Idade"] = ano_atual - trabalhador['Ano de nascimento']
trabalhador["CTPS"] = int(input('Digite a carteira de trabalho do trabalhador: '))

if trabalhador['CTPS'] != 0:
     trabalhador["Ano de contratação"] = int(input('Digite o ano de contratação do trabalhador: '))
     trabalhador["Salário"] = float(input('Digite o salário do trabalhador: '))
     trabalhador["Idade para a aposentadoria"] = (trabalhador["Ano de contratação"] - trabalhador["Ano de nascimento"]) + 35
else:
     del trabalhador['CTPS']
     
print(f'\n{'Informações':-^50}')
for k, v in trabalhador.items():
     print(f'{k}: {v}')
print(f'{'':-^50}')