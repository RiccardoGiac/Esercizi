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
print("---------------------------------------")

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
print("---------------------------------------")

"""
9-4. Number Served: Start with your program from Exercise 9-1. Add an attribute called number_served with a default value of 0. 
Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again. 
Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a new number and print the value again. 
Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. 
Call this method with any number you like that could represent how many customers were served in, say, a day of business. 
"""

class Restaurant():

    def __init__(self,restaurant_name : str, cuisine_type : str) -> None:
        self.restaurant_name : str = restaurant_name
        self.cuisine_type : str = cuisine_type
        self.number_served : int = 0
    
    def describe_restaurant(self):
        print(f"Name= {self.restaurant_name}, cuisine type= {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!") 

    def set_number_served(self,number_served : int):
        self.number_served = number_served  

    def increment_number_served(self):
        self.number_served += 1      

r1: Restaurant = Restaurant(restaurant_name="PizzaPizza", cuisine_type="Pizzeria")
r1.describe_restaurant()
r1.number_served = 4
print(f"Number served = {r1.number_served}")
r2: Restaurant = Restaurant(restaurant_name="VillaNuova", cuisine_type="Chic")
r2.describe_restaurant()
r2.number_served = 200
print(f"Number served = {r2.number_served}")
r3: Restaurant = Restaurant(restaurant_name="Tavola", cuisine_type="Tavola Calda")
r3.describe_restaurant()
r3.number_served = 60
print(f"Number served = {r3.number_served}")
r1.increment_number_served()
r1.describe_restaurant()
print(f"Number served = {r1.number_served}")


print("---------------------------------------")

"""
9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. 
Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
Write another method called reset_login_attempts() that resets the value of login_attempts to 0. 
Make an instance of the User class and call increment_login_attempts() several times. 
Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.
"""
class User:

    def __init__(self, first_name: str, last_name: str, date_of_birth : str) -> None:
        self.first_name : str = first_name
        self.last_name : str = last_name
        self.date_of_birth : str = date_of_birth
        self.login_attempts : int = 0

    def describe_user(self):
        print(f"Name= {self.first_name}, last name= {self.last_name}, date of birth = {self.date_of_birth}")

    def greet_user(self):
        print(f"Hello, {self.first_name}, how are you?")
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1: User = User(first_name="Riccardo",last_name="Giacalone",date_of_birth="28/06/1996")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)
user1.describe_user()
user1.greet_user()

print("---------------------------------------")

