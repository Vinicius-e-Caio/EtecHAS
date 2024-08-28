def ExcluirAl(nomeAl: str) -> None:
    if nomeAl in notas:
        try:
            del notas[nomeAl]
            print(f"Aluno {nomeAl} excluído com sucesso!")
        except:
            print("Ocorreu um erro ao tentar excluir o aluno.")
    else:
        print(f"Aluno {nomeAl} não encontrado!")

notas = {
    'lara': 1.0,
    'lara3': 1.0,
    'lara4': 1.0,
    'lara5': 1.0,
    'lara6': 1.0,
    'lara7': 1.0,
    'lara8': 1.0,
    'lara9': 1.0
}

while True:
    nameAl = input("Digite o nome do Aluno: ")
    if not nameAl.isalpha():
        print("Nome inválido!!")
        continue
    break
ExcluirAl(nameAl)
    
