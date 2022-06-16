poluicao = float(input("Informe o índice de poluição: "))

if poluicao >= 0.3 and poluicao < 0.4:
    print("Grupo 1 suspender atividades.")
if poluicao >= 0.4 and poluicao < 0.5:
    print("Grupo 2 suspender as atividades:")
if poluicao >= 0.5:
    print("Todos os grupos suspender as atividades.")
if poluicao < 0.3:
    print("Níveis aceitáveis.")