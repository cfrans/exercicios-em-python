numero = int(input("Informe um número: "))
while numero < 1 and numero > 10:
    print("Número deve ser de 1 a 10")
    numero = int(input("Informe um número: "))

print("Tabuada de {0}:".format(numero))
for i in range(1, 11):
    valor = numero * i
    print("{0} X {1} = {2}".format(i, numero, valor))
