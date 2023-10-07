import random
print("{:-^30}".format('Exercício 20'))
aluno1 = input("Digite o nome de um(a) aluno(a): ")
aluno2 = input("Digite o nome de um(a) aluno(a): ")
aluno3 = input("Digite o nome de um(a) aluno(a): ")
aluno4 = input("Digite o nome de um(a) aluno(a): ")
alunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(alunos)
print("{:=^30}\n{:^30}\n{:=^30}".format('', 'ORDEM:', ''))
print(alunos)
print("{:=^30}".format(''))