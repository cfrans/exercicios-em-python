maior = -999
menor = 9999
soma = 0
for i in range(1,11):
    valor = int(input("Informe o valor {0}/10: ".format(i)))
    while valor < 0:
        valor = int(input("Informe o valor {0}/10: ".format(i)))
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
    soma = soma + valor
print("Maior: {0}".format(maior))
print("Menor: {0}".format(menor))
print("Média: {0}".format(soma / 10))
