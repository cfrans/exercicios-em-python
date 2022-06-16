vetor = []
#soma = 0

for n in range(0,20):
    valor = int(input("Digite o valor {0}/20 para o vetor: ".format(n+1)))
    vetor.append(valor)
    #soma = soma + valor

print("Soma total: {0}".format(sum(vetor)))