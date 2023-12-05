print(f"{"Exercício 90":-^50}")
aluno = dict()
aluno["Nome"] = str(input('Digite o nome do aluno: '))
aluno["Média"] = float(input('Digite a média do aluno: '))
if(aluno["Média"] >= 5 ):
     aluno["Situação"] = 'Aprovado'
else:
     aluno['Situação'] = 'Reprovado'
for k, v in aluno.items():
     print(f'{k}: {v}')