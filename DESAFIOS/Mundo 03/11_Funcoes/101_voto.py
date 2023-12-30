print(f'{'Exercício 101':-^50}')
from datetime import datetime
ano_atual = datetime.now().year

def voto(ano_de_nascimento):
     idade = ano_atual - ano_de_nascimento
     if idade > 18 and idade < 65:
          return "VOTO OBRIGATÓRIO"
     elif idade >= 16 or idade >= 65:
          return "VOTO OPCIONAL"
     else:
          return "NÃO VOTA"

ano_de_nascimento = int(input('Digite o seu ano de nascimento: '))
print(f'Com {ano_atual - ano_de_nascimento} anos: {voto(ano_de_nascimento=ano_de_nascimento)}')
