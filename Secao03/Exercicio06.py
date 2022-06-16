horas = float(input("Insira a quantidade de horas trabalhadas no mês: "))
valor_hora = int(input("Insira o valor ganho por hora: "))
salario = horas * valor_hora
print("O salário deste mês será de: R$ {0:.2f}".format(salario))