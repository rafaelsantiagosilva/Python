print(f'{"\033[m"}{"Exercício 106":=^60}')
print(f"{'\033[30;42m'}{"~"*60}")
print(f'{"Sistema de Ajuda PyHelp":^60}')
print(f"{'\033[30;42m'}{"~"*60}")
while(True):
     answer = str(input(f"{'\033[m'}Função ou biblioteca (fim para parar): ")).upper()
     if(answer == "FIM"):
          break
     else:
          print(f'{'\033[30;47m'} {help(answer.lower())}')
          