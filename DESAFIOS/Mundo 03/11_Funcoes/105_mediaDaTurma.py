print(f'{'Exercício 105':-^50}')

def ler_notas(* notas, situacao = False):
     '''
     Lê as notas de indeterminada quantidade de alunos e 
     diz a média das notas, a maior nota e a menor nota.

     Além das notas (números reais), tem que se passar a situação:
     ler_notas(0, 0, 0, 0, situacao=True) ou somente deixar sem 
     situacao.

     Caso tenha o valor "True", também irá mostrar a situação média
     dos alunos.
     '''

     info = dict()
     info["Notas"] = notas
     media=0
     for i in range(0, len(notas)):
          media+=notas[i]
     media /= len(notas)
     info["Média"] = media
     info["Menor nota"] = min(notas)
     info["Maior nota"] = max(notas)
     if situacao:
          if media < 5:
               situacao = "RUIM"
          elif media <= 7:
               situacao = "RAZOÁVEL"
          elif media <= 9:
               situacao = "BOA"
          else: 
               situacao = "MUITO BOA"
          info["Situação"] = situacao
     for k, v in info.items():
          print(f'{k}: {v}')
     

ler_notas(5, 5, 5, 5)
print('\n')
ler_notas(6.5, 10, 9, 8, 7, 2, situacao=True)
print('\n')
ler_notas(10, 10, 10, 10, situacao=True)

# help(ler_notas)