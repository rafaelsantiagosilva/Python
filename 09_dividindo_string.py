print("{:-^30}".format('Aula 09'))
frase = "Curso em Vídeo Python"
print(frase, '\n')
    #Dividindo em várias listas
frase = frase.split()
print("Palavra 1:", frase[0])
print("Palavra 2:", frase[1])
print("Palavra 3:", frase[2])
print("Palavra 4:", frase[3])
    # Juntando as várias listas
frase = ' '.join(frase)
print("Juntando tudo:", frase)