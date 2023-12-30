from urllib.request import urlopen
print(f'{'Exercício 114':=^50}')
try:
     urlopen('https://pudim.com.br/')
except Exception as error:
     print("O site do Pudim não está acessível!")
else: 
     print("O site do Pudim está acessível!")