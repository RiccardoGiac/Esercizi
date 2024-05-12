
class Animal:

    def __init__(self,name: str,species: str,age: int,height: float,width: float,preferred_habitat: str):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100*(1/age),3)
        self.area = round(width * height,3)
    
class Fence:

    def __init__(self,area: float,temperature: float,habitat: str):
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals_inside : list[Animal] = []

class Zookeeper:

    def __init__(self,name: str,surname: str,id: str):
        self.name = name
        self.surname = surname
        self.id = id 

    def add_animal(self,animal:Animal,fence:Fence):
        if fence.area - animal.area >= 0 and animal.preferred_habitat == fence.habitat:
            fence.area -= animal.area
            fence.animals_inside.append(animal)
        else:
            print(f"Cannot add {animal.name} in this fence.")

    def remove_animal(self,animal:Animal,fence:Fence):
        if animal in fence.animals_inside:
            fence.animals_inside.remove(animal)
            fence.area += animal.area
        else:
            print("Animal is not in this fence")


    def feed(self,animal:Animal):
        pass

    def clean(self,fence:Fence):
        pass
        
class Zoo:

    def __init__(self,fences: Fence, zoo_keepers: Zookeeper):
        self.fences = fences
        self.zoo_keepers = zoo_keepers

    def describe_zoo(self):
        pass

    ######## TESTS #############
    a1 : Animal = Animal("pippo", "lupo",5, 23.3, 10, "Mountain")
    f1 : Fence = Fence(1000,20,"Mountain")
    zk1: Zookeeper = Zookeeper("Gino", "Baglio", "135G")
    zk1.add_animal(a1,f1)
    f2: Fence = Fence(2000,30,"Savana")
    zk1.remove_animal(a1,f2)