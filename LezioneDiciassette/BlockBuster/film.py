#Riccardo Giacalone

class Film:

    def __init__(self,id:int,title:str) -> None:
        
        self.id: int = id
        self.title: str = title

    
    def setID(self,id:int):
        self.id = id
    
    def setTitle(self,title:str):
        self.title = title

    def getID(self)->int :
        return self.id
    def getTitle(self)->str :
        return self.title
    
    def isEqual(self,otherFilm:str)->bool :
        if self.title == otherFilm:
            return True
        return False




