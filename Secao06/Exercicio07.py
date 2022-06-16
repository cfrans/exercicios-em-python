n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))
n3 = int(input("Insira o terceiro número: "))
n4 = int(input("Insira o quarto número: "))

q1 = n1 ** 2
q2 = n2 ** 2
q3 = n3 ** 2
q4 = n4 ** 2

if q3 > 1000:
    print(q3)
else:
    print(n1, q1)
    print(n2, q2)
    print(n3, q3)
    print(n4, q4)