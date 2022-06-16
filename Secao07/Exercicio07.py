sit1 = 0
sit2 = 0
sit3 = 0
sit4 = 0
total = 0
id = int(input("Informe o ID do mouse: "))
while id != 0:
    print("Identifique o defeito:")
    print("1 - Necessita de esfera")
    print("2 - Necessita de limpeza")
    print("3 - Necessita troca do cabou ou conector")
    print("4 - Quebrado ou unitilizado")
    defeito = int(input("Digite o defeito: "))
    if defeito == 1:
        sit1 = sit1 + 1
    elif defeito == 2:
        sit2 = sit2 + 1
    elif defeito == 3:
        sit3 = sit3 + 1
    elif defeito == 4:
        sit4 = sit4 + 1
    elif defeito > 4 or defeito < 0:
        print("Defeito desconhecido.")
    total = total + 1
    id = int(input("Informe o ID do mouse (ou 0 para encerrar): "))
perc_sit1 = (sit1 * 100) / total
perc_sit2 = (sit2 * 100) / total
perc_sit3 = (sit3 * 100) / total
perc_sit4 = (sit4 * 100) / total
print("Quantidade total de mouses: {0} un.".format(total))
print("Situação                                            Quantidade             Percentual")
print("1 - Necessita de esfera:                             {0} un.                   {1:.2f}%".format(sit1, perc_sit1))
print("2 - Necessita de limpeza:                            {0} un.                   {1:.2f}%".format(sit2, perc_sit2))
print("3 - Necessita de troca do cabou ou conector:         {0} un.                   {1:.2f}%".format(sit3, perc_sit3))
print("4 - Quebrado ou unitilizado:                         {0} un.                   {1:.2f}%".format(sit4, perc_sit4))