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

"""
9-3. Users: Make a class called User. Create two attributes called first_name 
and last_name, and then create several other attributes that are typically 
stored in a user profile. Make a method called describe_user() that prints 
a summary of the user’s information. Make another method called greet_user() 
that prints a personalized greeting to the user. Create several instances 
representing different users, and call both methods for each user.
"""
class User:

    def __init__(self, first_name: str, last_name: str, date_of_birth : str) -> None:
        self.first_name : str = first_name
        self.last_name : str = last_name
        self.date_of_birth : str = date_of_birth

    def describe_user(self):
        print(f"Name= {self.first_name}, last name= {self.last_name}, date of birth = {self.date_of_birth}")

    def greet_user(self):
        print(f"Hello, {self.first_name}, how are you?")

user1: User = User(first_name="Riccardo",last_name="Giacalone",date_of_birth="28/06/1996")
user1.describe_user()
user1.greet_user()