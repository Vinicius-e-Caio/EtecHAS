from os import system
from time import sleep

# Functions - For tests
def VerifyThis(newAluno, newNota) -> bool:
    newNota = newNota.replace(',', '.')
    newNota = float(newNota)
    if newNota < 0 or newNota > 10:
        print("Nota inválida.\n")
        return False
    return False

# Dicts / Variables
notas = {
    'lara2': 1.0,
    'lara3': 1.0,
    'lara4': 1.0,
    'lara5': 1.0,
    'lara6': 1.0,
    'lara7': 1.0,
    'lara8': 1.0,
    'lara9': 13.0
}

while True:
    contador = 0
    for keys in notas.keys():
        contador += 1
    if contador == 10:
        print("Limite de alunos atingido!")
        system("pause")
        continue
    system("cls")
    newAluno = input("Aluno: ")
    if newAluno in notas:
        print(f"Já existe um aluno com esse nome.\n")
        system("pause")
        continue
    if not newAluno.isalpha():
        print(f"Nomes só podem conter letras.\n")
        system("pause")
        continue
    newNota = input("Digite a Nota: ")
    if newNota.isdigit():
        print(f"Notas só podem conter números.\n")
        system("pause")
        continue
    VerifyThis(newAluno, newNota)

    while True: 
        system("cls")
        print(f"Aluno: {newAluno} \nNota: {newNota}")
        confirm = input("Confirma? (S/N): ")
        match confirm.upper():
            case 'S':
                notas[newAluno] = newNota
                print(f'Adicionado! \n')
                system("pause")
                system("cls")
                break
            case 'N':
                break
            case _:
                print("Digite um valor válido.")
        break
    while True:
        retry = input("Adicionar outro? (S/N): ")
        match confirm.upper():
            case 'S':
                break
            case 'N':
                retry == False
                break
            case _:
                print("Digite um valor válido.")
                break    
            

