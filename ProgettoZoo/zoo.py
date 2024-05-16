
class Animal:

    def __init__(self,name: str,species: str,age: int,height: float,width: float,preferred_habitat: str):
        self.name : str = name
        self.species : str = species
        self.age : int = age
        self.height : float = height
        self.width : float = width
        self.preferred_habitat : str = preferred_habitat
        self.health : float= round(100*(1/age),3)
        self.area : float = round(width * height,3)
        self.fence : Fence = None
    
    def __str__(self) -> str:
        return f"Animal(name={self.name},species={self.species},age={self.age})"

class Fence:

    def __init__(self,area: float,temperature: float,habitat: str):
        self.area : float = area 
        self.temperature : float = temperature
        self.habitat : str = habitat
        self.animals_inside : list[Animal] = []
        self.tot_area : float = area
        
        
    def __str__(self) -> str:
        return f"Fence(area={self.tot_area},temperature={self.temperature},habitat={self.habitat})"

class Zookeeper:


    def __init__(self,name: str,surname: str,id: str):
        self.name : str = name
        self.surname : str = surname
        self.id : str = id

    def add_animal(self,animal:Animal,fence:Fence):
        if fence.area - animal.area >= 0 and animal.preferred_habitat.casefold() == fence.habitat.casefold() and animal.fence == None:
            fence.area -= animal.area
            fence.animals_inside.append(animal)
            animal.fence = fence
        else:
            print("Cannot add animal")

    def remove_animal(self,animal:Animal,fence:Fence):
        if animal in fence.animals_inside:
            fence.animals_inside.remove(animal)
            fence.area += animal.area
        else:
            print("Animal is not in this fence")

    def feed(self,animal:Animal):
        animal_area_after: float = round(animal.area + (2 * animal.area) / 100,3)
        if (animal.fence and (animal.fence.area + animal.area) - animal_area_after >= 0) or not animal.fence:  
            animal.fence.area = (animal.fence.area + animal.area) - animal_area_after                          #qui toglie quel 2% dell' area dell'animale dall'area residua della fence
            animal.area = animal_area_after
            animal.health = round(animal.health + animal.health /100,3)
        else:
            print("Cannot feed the animal.") 

    def clean(self,fence:Fence)-> float:
        sum_area_animals: float = 0
        if fence.area == 0:
            return fence.tot_area
        else:
            for a in fence.animals_inside:
                sum_area_animals += a.area
            return round(sum_area_animals / fence.area, 3)
        
    def __str__(self) -> str:
        return f"ZooKeeper(name={self.name},surname={self.surname},id={self.id})"
                   

class Zoo:
    def __init__(self, fences : list[Fence], zoo_keepers : list[Zookeeper] ) -> None:
        self.fences : list[Fence] = fences
        self.zoo_keepers : list [Zookeeper] = zoo_keepers
    
    def describe_zoo(self):
        print("Guardians:")
        for k in self.zoo_keepers:
            print(f"{k}\n")
        print("Fences:")
        for f in self.fences:
            print(f"{f}\n")
            print("With animals:")
            if f.animals_inside:
                for j in f.animals_inside:  
                     print(j)
            else:
                print("Fence is empty.")
            print("\n" + "#" * 30)

######TEST########VEDI SE CI SONO ALTRI TEST DA FARE SE NO MANDA



zk: Zookeeper = Zookeeper("Luigi", "fgas","131")
zk2: Zookeeper = Zookeeper("Marco", "afdes","545")
a2: Animal = Animal("animalo2","animala",5,20,5,"mountain")
a1: Animal = Animal("animalo","animala",4,5,6,"Foresta")
a3: Animal = Animal("animalo3", "animala", 5,2,5,"Foresta")
f1: Fence = Fence(2000,20,"Foresta")
f2: Fence = Fence(300,10,"Mountain")
zk.add_animal(a1,f1)
zk2.add_animal(a2,f2)

print("--------Test clean-------")
print(zk.clean(f1))
print("-------------------------")
zoo1 : Zoo = Zoo([f1,f2],[zk])
zoo2 : Zoo = Zoo([f2],[zk2])
zoo1.describe_zoo()
print("zoo 2 -------")
zoo2.describe_zoo()
print("TEST HEALTH E AREA ANIMALE DOPO FEED")
print(a1.health)
print(a1.area)
zk.feed(a1)
print(a1.health)
print(a1.area)
print("--------------------------zooooo1")
zk.add_animal(a3,f1)
zk.add_animal(a3,f2)

zoo1.describe_zoo()


