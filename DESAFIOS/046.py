from time import sleep
print('{:-^50}'.format('Exercício 46'))
for i in range(10, 0, -1):
    print(i)
    sleep(0.1)
print('{}{}BOOM{} BLAUU{} KAPOW!'.format('\033[1m', '\033[31m', '\033[32m', '\033[34m'))