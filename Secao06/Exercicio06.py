extra = 0
codigo = int(input("Insira o código do funcionário: "))
horas = int(input("Insira a quantidade de horas trabalhadas: "))

if horas > 50:
    extra = horas - 50
    horas = horas - extra

print("Funcionário {0}:".format(codigo))
print("Salário: R$ {0:.2f}".format(horas * 10))
print("Extra: R$ {0:.2f}".format(extra * 20))