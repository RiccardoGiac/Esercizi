#Riccardo Giacalone

"""
9-1. Restaurant: Make a class called Restaurant. 
The __init__() method for Restaurant should store two attributes: 
a restaurant_name and a cuisine_type. Make a method called 
describe_restaurant() that prints these two pieces of information, 
and a method called open_restaurant() that prints a message indicating 
that the restaurant is open. Make an instance called restaurant from your 
class. Print the two attributes individually, and then call both methods.
"""

class Restaurant():

    def __init__(self,restaurant_name : str, cuisine_type : str) -> None:
        self.restaurant_name : str = restaurant_name
        self.cuisine_type : str = cuisine_type
    
    def describe_restaurant(self):
        print(f"Name= {self.restaurant_name}, cuisine type= {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")  

r1: Restaurant = Restaurant(restaurant_name="PizzaPizza", cuisine_type="Pizzeria")
r1.describe_restaurant()
r2: Restaurant = Restaurant(restaurant_name="VillaNuova", cuisine_type="Chic")
r2.describe_restaurant()
r3: Restaurant = Restaurant(restaurant_name="Tavola", cuisine_type="Tavola Calda")
r3.describe_restaurant()
