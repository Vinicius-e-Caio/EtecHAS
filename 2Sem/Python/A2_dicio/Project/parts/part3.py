def listAluno() -> None:
    print("Alunos cadastrados:")
    for aluno, nota in notas.items():
        print(f"{aluno}: {nota}")

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
listAluno()