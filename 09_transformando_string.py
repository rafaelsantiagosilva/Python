print("{:-^30}".format('Aula 09'))
frase = 'Olá Mundo! Me livrei da maldição :D'
print(frase, '\n')
    # Substituindo
nome = input("Digite seu nome: ")
frase = frase.replace("Mundo", nome)
print(frase)
    # Deixando Maiúscula
print("Em maiúscula, a frase fica: '{}'".format(frase.upper()))
    # Deixando minúscula
print("Já em minúscula: '{}'".format(frase.lower()))
    # Primeira letra maiúscula
print("Com a primeira em maiúscula somente: '{}'".format(frase.capitalize()))
    # Primeira letra de cada palavra em maiúscula
print("Primeira letra em cada palavra maiúscula: '{}'".format(frase.title()))
print("\nSubstituindo frase...")
frase = ' Aprendendo Python   '
print(frase)
    # consertando esses espaços
frase = frase.rstrip()
print("Consertando os espaços a direita: ", frase)
frase = frase.lstrip()
print("Consertando os espaços a esquerda: ", frase)
frase = frase.strip()
print("Frase consertada:\n{}".format(frase))