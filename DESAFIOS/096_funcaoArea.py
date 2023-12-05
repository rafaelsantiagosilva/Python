print(f'{'Exercício 96':-^70}')

# Função de calcular área
def calcular_area(largura, comprimento):
     return largura * comprimento

largura = float(input('Digite a largura do terrreno [m]: '))
comprimento = float(input('Digite o comprimento do terrreno [m]: '))
print(f'A área do terreno é de {calcular_area(largura=largura, comprimento=comprimento)}m²')