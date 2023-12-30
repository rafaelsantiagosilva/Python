from random import randint
print("{:-^30}".format('Exercício 19'))
num_aluno = randint(1, 4)
print("{:=^30}\n{:^30}\n{:=^30}".format('', 'ALUNO SORTEADO:', ''))
print("Número: {}\n{:=^30}".format(num_aluno, ''))