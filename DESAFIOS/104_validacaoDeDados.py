print(f'{'Exercício 104':-^50}')

def leia_int(num):
     erro = True
     pergunta = "Digite um número inteiro: "
     while erro:
          try:
               num = int(input(pergunta))
               erro = False
          except ValueError:
               pergunta = f'{'\033[31m'}ERRO: Digite um número inteiro: '
     return num

numero = int(0)
print(f'{'\033[m'}\nO número digitado foi:', leia_int(numero))