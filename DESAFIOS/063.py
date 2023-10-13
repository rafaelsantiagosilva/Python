print('{:-^50}'.format('Exercício 63'))
n = int(input('Até qual termo vai a sequência de Fibonacci?\nR:'))
print('\n{:=^50}\n{:^50}\n{:=^50}'.format('', 'SEQUÊNCIA DE FIBONACCI', ''))
a1 = 0
a2 = 1
print(a1)
print(a2)
i=0
while i < n-2:
    an = a1 + a2
    print(an)
    a1 = a2
    a2 = an
    i+=1  
print('{:=^50}'.format(''))