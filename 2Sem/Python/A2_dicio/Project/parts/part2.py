def editarAluno(nomeAluno, newNota) -> None:


notas = {
    'lara2': 1.0,
    'lara3': 1.0,
    'lara4': 1.0,
    'lara5': 1.0,
    'lara6': 1.0,
    'lara7': 1.0,
    'lara8': 1.0,
    'lara9': 1.0
}
aluno = str(input("Digite o Nome do aluno para alterar o aluno: "))
if not aluno.isalpha():
    print("Nome inválido!!")
aluno = float(input("Digite a nova nota: "))
