print(f'{"Exercício 85":-^50}')
num = 0
nums = [[], []]
for i in range(0,7):
     num = int(input(f'Digite o {i+1}ºnúmero: '));
     if num % 2 != 0:
          nums[0].append(num);
     else:
          nums[1].append(num);
nums[0].sort();
nums[1].sort();
print("Os ímpares são: ", end='')
for i in nums[0]:
     print(i, ' ', end='')
print('\nOs pares são: ', end='')
for i in nums[1]:
     print(i, ' ', end='')