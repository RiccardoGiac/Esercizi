
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
    
class Fence:

    def __init__(self,area: float,temperature: float,habitat: str):
        self.area : float = area
        self.temperature : float = temperature
        self.habitat : str = habitat
        self.animals_inside : list[Animal] = []
    
    def get_area_occupied(self):
        area_occ: float = 0
        for animal in self.animals_inside:
            area_occ += animal.area
        return area_occ

class Zookeeper:

    def __init__(self,name: str,surname: str,id: str):
        self.name : str = name
        self.surname : str = surname
        self.id : str = id 

    def add_animal(self,animal:Animal,fence:Fence):
        if fence.area - animal.area >= 0 and animal.preferred_habitat.casefold() == fence.habitat.casefold() and not animal.fence:
            fence.area -= animal.area
            fence.animals_inside.append(animal)
            animal.fence = fence
        else:
            print(f"Cannot add {animal.name} in this fence.")

    def remove_animal(self,animal:Animal,fence:Fence):
        if animal in fence.animals_inside:
            fence.animals_inside.remove(animal)
            fence.area += animal.area
        else:
            print("Animal is not in this fence")


    def feed(self,animal:Animal):
        animal_area_after: float = round(animal.area + (2 * animal.area) / 100,3)
        if (animal.fence and (animal.fence.area + animal.area) - animal_area_after >= 0) or not animal.fence:  #qui toglie quel 2% dell' area dell'animale dall'area residua della fence
            animal.area = animal_area_after
            print(animal_area_after)
            animal.health = round(animal.health + animal.health /100,3)
            print(animal.health)
        else:
            print("Cannot feed the animal.")
            


    def clean(self,fence:Fence)-> float:
    
        area_tot : float = 0
       
        area_tot = fence.area + fence.get_area_occupied() #perchè fence area viene usata anche in remove
                                    #quindi per trovare area tot -> fence.area + area occ da animali
                                    #fence.area è area residua
        if area_tot == 0:
            return fence.area + fence.get_area_occupied()
        else:
            return round(fence.get_area_occupied() / fence.area, 3)

        
            
        
class Zoo:

    def __init__(self,fences: Fence, zoo_keepers: Zookeeper):
        self.fences : Fence = fences
        self.zoo_keepers : Zookeeper = zoo_keepers

    def describe_zoo(self):
        pass

    ######## TESTS #############
    a1 : Animal = Animal("pippo", "lupo",5, 950, 1, "Mountain")
    a2 : Animal = Animal("rock", "aquila", 2, 7, 10,"mountain")
    f1 : Fence = Fence(1000,20,"Mountain")
    zk1: Zookeeper = Zookeeper("Aldo", "Baglio", "135G")
    print(a1.area)
    zk1.add_animal(a1,f1)
    zk1.feed(a1)
    zk1.add_animal(a2,f1)
    f2: Fence = Fence(2000,30,"Savana")
    print(zk1.clean(f1))
    print(f1.get_area_occupied())
