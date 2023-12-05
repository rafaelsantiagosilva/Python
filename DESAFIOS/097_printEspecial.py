print(f'{'Exercício 97':-^70}')

# Definindo a função
def print_especial(msg):
     print(f'\n{'~'* len(msg)}\n{msg}\n{'~'* len(msg)}')

text = str(input('Digite o texto para a mensagem: '))
print_especial(text)  