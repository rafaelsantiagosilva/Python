from random import randint
print('{:-^50}'.format('Exercício 45'))
# Titulo
print('\n{:^50}'.format('Vamos jogar Jokenpô?'))
# Legenda
print('\n{:-^25}'.format('Legenda'))
print('Pedra [1]')
print('Papel [2]')
print('Tesoura [3]')
print('{:-^25}'.format(''))
# Fim legenda
opc_user = int(input('Digite uma das opções acima: '))
if str(opc_user) in '1 2 3':
    # Escolhendo opção do computador
    opc_npc = randint(1, 3)
    # Verificando vitória...
    if opc_user == 1 and opc_npc == 3:
        condicao = 'VITÓRIA'
    elif opc_user == 3 and opc_npc == 1:
        condicao = 'DERROTA'
    elif opc_user > opc_npc:
        condicao = 'VITÓRIA'
    elif opc_user < opc_npc:
        condicao = 'DERROTA'
    else:
        condicao = 'EMPATE'
    # Verificando movimento do usuário
    if opc_user == 1:
        opc_user = 'Pedra'
    elif opc_user == 2:
        opc_user = 'Papel'
    else:
        opc_user = 'Tesoura'
    
    # Verificando movimento do computador
    if opc_npc == 1:
        opc_npc = 'Pedra'
    elif opc_npc == 2:
        opc_npc = 'Papel'
    else:
        opc_npc = 'Tesoura'

    # Imprimindo resultado
    print('\n{:=^50}\n{:^50}\n{:=^50}'.format('', 'RESULTADO', ''))
    print('{:^50}'.format(condicao))
    print('{:^25}{:^25}'.format('Você', 'Computador'))
    print('{:^25}{:^25}'.format(opc_user, opc_npc))
    print('{:=^50}'.format(''))
# Opção inválida
else:
    print('Eiii, só pode digitar uma daquelas opções :(')