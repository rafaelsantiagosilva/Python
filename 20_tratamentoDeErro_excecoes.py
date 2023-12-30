print(f'{'Aula 20':=^50}')

try: # Tente...
     a = float(input('Digite um número: '))
     b = float(input('Digite um número: '))
     resultado = a/b

except (ValueError, TypeError): #...mas se ocorrer um problema de tipo ou valor...
     print("TINHA QUE DIGITAR UM NÚMERO! ANIMAL...")

except ZeroDivisionError:
     print("Impossível dividir por zero!") #...mas se tentar dividir por zero...

except KeyboardInterrupt: #...mas se não informar os dados...
     print("Pq vc naum dize nauda? :(")

except Exception as error: # ..mas se ocorrer um problema
     print(f'Infelizmente tivemos um problema de {error.__class__}! D:')
else: #...senão ocorrer problema
     print('O resultado é de ' + resultado)
     
finally: #...por fim, com ou sem problema...
     print('Volte sempre! :D')

'''
Temos alguns erros/exceções como:
-> NameError: 
     Erro de nome, de variável com nome errado

-> ValueError: 
     Erro de valor, um int receber uma string, por exemplo

-> ZeroDivisionError: 
     Erro de divisão por zero

-> TypeError: 
     Erro de tipo

-> IndexError ou KeyError:   
     Erro da key ou casa do array

-> ModuleNotFindError: 
     Erro de módulo não encontrado
'''