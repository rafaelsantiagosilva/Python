print(f"{"Exercício 84":-^50}");
# Var
pessoa = list();
pessoas = list();
maior = menor = 0
opc = 'S';
while opc == 'S':
     pessoa.append(str(input("Nome: ")));
     pessoa.append(float(input("Peso: ")));
     if len(pessoas) == 0:
          maior = menor = pessoa[1];
     else:
          if pessoa[1] > maior:
               maior = pessoa[1];
          if pessoa[1] < menor:
               menor = pessoa[1];
     pessoas.append(pessoa[:]);
     pessoa.clear();
     opc = str(input('Deseja continuar? [S/N]\nR:')).upper();
print("As pessoas cadastradas foram: \n", pessoas);
print(f"Você cadastrou {len(pessoas)} pessoas");
print(f"O maior peso foi de {maior}kg e o menor peso foi de {menor}kg")
print(f"As pessoas com maiores pesos são: ")
for pesos in pessoas:
     if pesos[1] == maior:
          print(pesos[0])
print(f"As pessoas com menores pesos são: ")
for pesos in pessoas:
     if pesos[1] == menor:
          print(pesos[0])