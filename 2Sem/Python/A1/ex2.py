import os
os.system("cls")
def to_separate(lista: list) -> None:
     listint = []
     listfloat = []
     liststr = []
     listbool = []
     for c in range(len((list))):
          tipo = type(list[c])
          if tipo == int:
               listint.append(list[c])
          elif tipo == str:
               liststr.append(list[c])
          elif tipo == float:
               listfloat.append(list[c])
          elif tipo == bool:
               listbool.append(list[c])
     print(listint, "\n",
           listfloat, "\n",
           liststr, "\n",
           listbool, "\n")

list = [45, 5.7, "Férias", True, False, 99, 34]
to_separate(list)