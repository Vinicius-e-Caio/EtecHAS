import os
os.system("cls")

def editarAluno(nomeAluno:  str, newNota: str) -> None:
    newNota = newNota.replace(",", ".")
    newNota = float(newNota)
    if newNota < 0 or newNota > 10:
        print("Nota inválida.\n")
        return None
    found = False
    for keys in notas.keys():
        if keys.lower() == nomeAluno.lower():
            found = True
    if not found:
        print(f"Aluno {nomeAluno.lower()} não encontrado!")
        return 
    try:
        notas[nomeAluno] = newNota
        print(f"Nota do aluno {nomeAluno.lower()} alterada com sucesso!")    
    except:
        print(f"Ocorreu um erro.")

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
aluno = str(input("Digite o nome do aluno para alterar sua nota: "))
if not aluno.isalpha():
    print("Nome inválido!!")
nota = input("Digite a nova nota: ")
if not nota.isdigit():
    print("Nota inválida!!")
editarAluno(aluno, nota)
