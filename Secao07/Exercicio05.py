nome = input("Informe o nome: ")
senha = input("Informe a senha: ")

while senha == nome:
    print("Senha não pode ser igual ao nome.")
    nome = input("Informe o nome: ")
    senha = input("Informe a senha: ")