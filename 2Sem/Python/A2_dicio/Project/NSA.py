from os import system
from time import sleep
system("cls")

# Dicts / Variables
notas = {
}


print("Bem vindo ao mini NSA")
print( """
    1 - Adicionar novo Aluno | Nota (limite 10 alunos)
    2 - Editar Aluno | Nota
    3 - Listar os Alunos
    4 - Excluir um Aluno
    5 - Calcular a média da turma
    6 - Consultar um aluno
    7 - Apagar todos os alunos da sala
""")
key = 1
while key != 0:
    option = int(input("Digite sua Opção: "))
    match option:
        case 1:
            # Prints
            system("cls")
            print("Você escolheu:") 
            sleep(1)
            print("1 - Adicionar novo Aluno | Nota")
            print("Lembre-se o limite é de 10 alunos")
            print("\n")
            sleep(1)
            system("pause")
            def VerifyThis(newAluno, newNota) -> bool:
                newNota = newNota.replace(',', '.')
                newNota = float(newNota)
                if newNota < 0 or newNota > 10:
                    print("Nota inválida.\n")
                    return False
                return False

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
                if not newNota.isdigit():
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
                break
        case 2:
            # Prints
            system("cls")
            print("Você escolheu:") 
            sleep(1)
            print("2 - Editar Aluno | Nota")
            print("\n")
            sleep(1)
            system("pause")

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
            while True:
                aluno = str(input("Digite o nome do aluno para alterar sua nota: "))
                if not aluno.isalpha():
                    print("Nome inválido!!")
                    continue
                nota = input("Digite a nova nota: ")
                if nota.isalpha():
                    print("Nota inválida!!")
                    continue
                editarAluno(aluno, nota)


        case 3:
            # Prints
            system("cls")
            print("Você escolheu:") 
            sleep(1)
            print("3 - Listar os Alunos")
            print("\n")
            sleep(1)
            system("pause")
            def listAluno() -> None:
                print("Alunos cadastrados:")
                if not notas.keys():
                    print("Nenhum aluno cadastrado!")
                    return None
                for aluno, nota in notas.items():
                    print(f"{aluno}: {nota}")
            listAluno()

        case 4:
            # Prints
            system("cls")
            print("Você escolheu:") 
            sleep(1)
            print("4 - Excluir um Aluno")
            print("\n")
            sleep(1)
            system("pause")

            def ExcluirAl(nomeAl: str) -> None:
                retry = False
                while True:
                    if nomeAl in notas:
                        try:
                            del notas[nomeAl]
                            print(f"Aluno {nomeAl} excluído com sucesso!")
                            break
                        except:
                            print("Ocorreu um erro ao tentar excluir o aluno.")
                            
                    else:
                        print(f"Aluno {nomeAl} não encontrado!")
                        confirmRetry = input("Quer tentar de novo? (S/N)")
                        match confirmRetry.upper():
                            case 'S':
                                nomeAl = str(input("Digite novamente: "))
                            case 'N':
                                break
                            case _:
                                print("Digite um valor válido.")
            while True:
                nameAl = input("Digite o nome do Aluno: ")
                if not nameAl.isalpha():
                    print("Nome inválido!!")
                    continue
                break
            ExcluirAl(nameAl)
    

        
        case 5:
            # Prints
            system("cls")
            print("Você escolheu:") 
            sleep(1)
            print("5 - Calcular a média da turma")
            print("\n")
            sleep(1)
            system("pause")

        case 6:
            # Prints
            system("cls")
            print("Você escolheu:") 
            sleep(1)
            print("6 - Consultar um aluno")
            print("\n")
            sleep(1)
            system("pause")
        
        case 7:
            # Prints
            system("cls")
            print("Você escolheu:") 
            sleep(1)
            print("7 - Apagar todos os alunos da sala")
            print("\n")
            sleep(1)
            system("pause")

        case _:
            print("DIgite uma opção válida")
