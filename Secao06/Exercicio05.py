excesso = 0
multa = 0
peso = float(input("Insira o peso dos peixes: "))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4

print("Peso: {0} kg".format(peso))
print("Excesso: {0} kg".format(excesso))
print("Multa: R$ {0:.2f}".format(multa))