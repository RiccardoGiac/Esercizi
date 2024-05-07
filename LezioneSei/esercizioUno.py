#Riccardo Giacalone
#Esercizio in aula 07/05/2024

class Person:                                                     

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)

#Print bob age
print(bob.age)

#If statement that prints the oldest of the two persons

if bob.age > alice.age:
    print("Bob is the oldest")
elif bob.age < alice.age:
    print("Alice is the oldest")
else:
    print("Bob and Alice have the same age")

#Create three other Persons. Make a list called people with all 5 Persons.

riccardo = Person("Riccardo", 27)
marco = Person("Marco", 19)
andrea = Person("Andrea", 20)

people: list = [alice,bob,riccardo,marco,andrea]

#Make a loop that finds and prints the youngest person's name
youngestAge: int = 2000
youngestName: str = ""
for person in people:
    if person.age < youngestAge:
        youngestAge = person.age
        youngestName = person.name
print(youngestName)

    