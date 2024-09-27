

mylist_1 = "['mario', 'gino','lucrezia']"

mylist_2 = ['mario', 'gino','lucrezia']


def SerializzaLista(lVar) -> str:
    return str(lVar)

def Deserializza(sVar) -> list:
    sVar = sVar.strip("[]").split(",")
    ls = []
    for i in sVar:
        i = i.strip(" ")
        ls.append(i.strip("'"))
    return ls
 


sProva = Deserializza(mylist_1)
if sProva == mylist_2:
    print("Procedura conclusa correttamente")

sProva1 = SerializzaLista(mylist_2)
if sProva1 == mylist_1:
    print("Procedura conclusa correttamente")

