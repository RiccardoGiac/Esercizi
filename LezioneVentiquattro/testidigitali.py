#Riccardo Giacalone

class Documento:

    def __init__(self) -> None:
        self.testo:str = None

    def getText(self)-> str:
        return self.testo
    
    def setText(self,nuovo_testo:str):
        self.testo = nuovo_testo
    
    def isInText(self,keyword:str)->bool:
        if keyword in self.testo:
            return True
        return False
    
class Email(Documento):

    def __init__(self, testo: str,mittente:str,destinatario:str,titolo:str) -> None:
        super().__init__(testo)
        self.mittente = mittente
        self.destinatario = destinatario
        self.titolo = titolo

    def getMittente(self)->str:
        return self.mittente
    def getDestinatario(self)->str:
        return self.destinatario
    def getTitolo(self)->str:
        return self.titolo
    
    def setMittente(self,nuovo_mittente:str):
        self.mittente = nuovo_mittente
    def setDestinatario(self,nuovo_destinatario:str):
        self.destinatario = nuovo_destinatario
    def setTitolo(self,nuovo_titolo:str):
        self.titolo = nuovo_titolo

    def getText(self) -> str:
        return f"Da: {self.mittente}, A: {self.destinatario}\nTitolo: {self.titolo}\nMessaggio: {self.testo}"

    def writeToFile(self,path:str):
        with open(path,"w") as document:
               document.write(self.getText())


class File(Documento):

    def __init__(self) -> None:
        super().__init__()
        self.nomePercorso:str = ""

 

