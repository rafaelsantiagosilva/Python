titulo = "Exercício 09"
print("{:-^40}".format(titulo))
numero =  int(input("Digite um número: "))
print("\n{:-^25}".format("-"))
print("A SUA TABUADA FICA EM:")
print("{:-^25}".format("-"))
i=0
while(i<=10):
    print("{} x {} = {}".format(numero, i, numero*i))
    i=i+1
print("{:-^25}".format("-"))