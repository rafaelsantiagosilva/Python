print("{:-^30}".format('Aula 09'))
frase = 'Olá Mundo! Me livrei da maldição :D'
# Escrevendo partes específicas das frases
print(frase[0])
    # Vai do 0 ao 9
print(frase[0:10])
print(frase[33:35])
    # Indo de 2 em 2
print(frase[9:21:2])
    # Todos antes do caractere 4
print(frase[:4])
    # Todos depois do caractere 4
print(frase[4:])
    # Todos depois do caractere 4, de 3 em 3
print(frase[4::3])
    # Tamanho da frase
print('\nTamanho da frase: ', len(frase))
    # Contando caracteres
letra_user = input("Digite uma letra: ")
qtd_user = frase.count(letra_user)
print('A letra "{}" aparece {} vezes\n'.format(letra_user, qtd_user))
qtd_user = frase.count(letra_user, 0, 10)
print("Nos primeiros 10 caracteres, a letra '{}' aparece {} vezes!".format(letra_user, qtd_user))
    # Achando conjuntos de caracteres
conjunto_user = input("Digite uma parte da frase: ")
print('"{}" começou no caractere {}'.format(conjunto_user, frase.find(conjunto_user)))
    # Vendo se o conjunto existe na frase
print("Essa parte existe na frase?", conjunto_user in frase)

