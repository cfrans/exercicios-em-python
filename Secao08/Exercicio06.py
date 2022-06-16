vetor = []
codigo = int(input("Informe o código: "))
if codigo > 0:
    for n in range(0,5):
        valor = float(input("Informe um valor real: "))
        vetor.append(valor)
    if codigo == 1:
        for n in vetor:
            print(n)
    if codigo == 2:
        vetor.reverse()
        for n in vetor:
            print(n)