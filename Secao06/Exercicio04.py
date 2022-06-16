altura = float(input("Informe sua altura: "))
sexo = input("Informe seu sexo M/F: ")

if sexo.lower() == 'm':
    peso_ideal = (72.7 * altura) - 58
elif sexo == 'F' or sexo == 'f': #mantive desta forma para ter exemplo de como usar o .lower ou fazer as verificações manualmente
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = 0
    print("Sexo não reconhecido.")
print("Seu peso ideal é {0:.2f} kg".format(peso_ideal))