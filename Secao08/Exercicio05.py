from operator import truediv


vetor = []
maiorde50 = False

for n in range(0,10):
    valor = int(input("Digite o valor {0}/10: ".format(n+1)))
    vetor.append(valor)

for n in vetor:
    if n > 50:
        print("Valor {0} maior que 50 na posição {1}".format(n, vetor.index(n)))
        maiorde50 = True

if maiorde50 == False:
    print("Não existem valores maiores do que 50.")