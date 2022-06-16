maior = 0
valor = int(input("Informe um valor: "))

while valor != 0:
    if valor > maior:
        maior = valor
    valor = int(input("Informe um valor (ou 0 para encerrar): "))

print("Maior valor: {0}".format(maior))