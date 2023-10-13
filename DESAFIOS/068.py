# Importando o gerador de números aleatórios
from random import randint

# Título do programa
print(f'{"Exercício 67":-^50}')

# Título do jogo
print('\n{:=^40}\n{:^40}\n{:=^40}'.format('', 'IMPAR OU PAR', ''))

# Declaração de variáveis
vitorias_comp = i = opc_user = num_user = num_comp = 0
resultado = opc_usertxt = opc_comptxt = ''
vitoria = False

# Começo do Jogo: Até o usuário vencer, o jogo vai rodar
while not vitoria:
    
    # Perguntando opção do usuário
    opc_user = int(input('\nDigite uma das opções: \nImpar[1]\Par[2]\nR:'))
    
    # Até o usuário digitar uma das opções, o jogo vai perguntar qual é a opção
    while opc_user != 1 and opc_user != 2:
        opc_user = int(input('\nPor favor, digite uma das opções: \nImpar[1]\Par[2]\nR:'))
    
    # "Convertendo" a opção em texto
    if opc_user == 1:
        opc_usertxt = "IMPAR"
        opc_comptxt = "PAR"
    else:
        opc_usertxt = "PAR"
        opc_comptxt = "IMPAR"
        
    # Pedindo para digitar um número de 0 a 10
    num_user = int(input('\nDigite um número de 0 a 10: '))
    
    # Até o usuário digitar um número de 0 a 10, o programa vai pedir 
    while num_user < 0 or num_user > 10:
        num_user = int(input('\nPor favor, digite um número de 0 a 10: '))
        
    # Definindo o número de 0 a 10 no computador
    num_comp = randint(0, 10)
    
    # Formatando e imprimindo opções
    print('\n{:^20}{:^20}'.format('VOCÊ: ' + str(opc_usertxt), 'COMPUTADOR: ' + str(opc_comptxt)))
    print('{:^20}{:^20}'.format(num_user, num_comp))
    resultado = num_user + num_comp
    
    # Dizendo o resultado da soma dos números digitados
    resposta = 'RESULTADO: ' + str(resultado)
    print('{:^40}'.format(resposta))
    
    # Verificando que venceu
    if resultado % 2 == 0 and opc_user == 2:
        vitoria = True
        resultado = 'VITÓRIA'
    elif resultado % 2 != 0 and opc_user == 1:
        vitoria = True
        resultado = 'VITÓRIA'
    else:
        vitoria = False
        vitorias_comp+=1
        resultado = 'DERROTA'
        
    # Imprimindo resultado
    print('{:^40}'.format(resultado))
print('{:=^40}'.format(''))
print(f'\nO computador venceu {vitorias_comp} vezes')