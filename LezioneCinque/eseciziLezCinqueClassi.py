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

"""9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. 
Write a class called IceCreamStand that inherits from the Restaurant 
class you wrote in Exercise 9-1  or Exercise 9-4. Either version of 
the class will work; just pick the one you like better. Add an attribute 
called flavors that stores a list of ice cream flavors. 
Write a method that displays these flavors. Create an instance of 
IceCreamStand, and call this method. 

"""

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name: str, cuisine_type: str,flavors: list[str]) -> None:
        super().__init__(restaurant_name, cuisine_type)

        self.flavors : list[str] = flavors

    def display_flavor(self):
        print(self.flavors)

icecream: IceCreamStand = IceCreamStand("Bagliori","Gelateria",["pistacchio","cioccolato","limone"])
icecream.display_flavor()

print("---------------------------------------")

"""
9-7. Admin: An administrator is a special kind of user. 
Write a class called Admin that inherits from the User class you 
wrote in Exercise 9-3 or Exercise 9-5. Add an attribute, privileges, 
that stores a list of strings like "can add post", "can delete post", 
"can ban user", and so on. Write a method called show_privileges() 
that lists the administrator’s set of privileges. 
Create an instance of Admin, and call your method. 
"""

class Admin(User):

    def __init__(self, 
                 first_name: str, 
                 last_name: str, 
                 date_of_birth: str,
                 ) -> None:
        super().__init__(first_name, last_name, date_of_birth)

        self.privileges: list[str] = ["can delete posts", "can add posts"]
        
    def show_privileges(self):

        print(self.privileges)



admin: Admin = Admin("Riccardo","Giaca","19/09/1998")
admin.show_privileges()


print("---------------------------------------")

"""
9-8. Privileges: Write a separate Privileges class. 
The class should have one attribute, privileges, that stores 
a list of strings as described in Exercise 9-7. 
Move the show_privileges() method to this class. 
Make a Privileges instance as an attribute in the Admin class. 
Create a new instance of Admin and use your method to show its privileges.
"""

class Admin(User):

    def __init__(self, 
                 first_name: str, 
                 last_name: str, 
                 date_of_birth: str,
                 ) -> None:
        super().__init__(first_name, last_name, date_of_birth)

        self.privileges: Privileges = Privileges()

class Privileges:

    def __init__(self, privileges: list[str]=[]) -> None:
        self.privileges : list[str] = privileges
    
    def show_privileges(self):
        print(self.privileges)

admin1 : Admin = Admin("Giacomo","gsegeg","21/03/1993")
admin1.privileges.privileges = ["can add post", "can delete post"]
admin1.privileges.show_privileges()

print("---------------------------------------")

"""
9-10. Imported Restaurant: Using your latest Restaurant class, 
store it in a module. Make a separate file that imports Restaurant. 
Make a Restaurant instance, and call one of Restaurant’s methods to 
show that the import statement is working properly.
"""
###########################

"""
9-11. Imported Admin: Start with your work from Exercise 9-8. 
Store the classes User, Privileges, and Admin in one module. 
Create a separate file, make an Admin instance, and 
call show_privileges() to show that everything is working correctly.
"""
###########################

"""
9-12. Multiple Modules: Store the User class in one module, 
and store the Privileges and Admin classes in a separate module. 
In a separate file, create an Admin instance and call show_privileges() 
to show that everything is still working correctly.
"""
##############DA FARE###############

"""
9-13. Dice: Make a class Die with one attribute called sides, 
which has a default value of 6. Write a method called roll_die() 
that prints a random number between 1 and the number of sides 
the die has. Make a 6-sided die and roll it 10 times. 
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""
from random import randint
class Die:

    def __init__(self,sides:int = 6) -> None:
        self.sides:int = sides

    def roll_die(self):
        print(randint(1,self.sides))
    
die6:Die = Die()
die6.roll_die()
print("10 rolls 6 sides:\n")
i : int = 0
while i < 10:
    die6.roll_die()
    print("---")
    i += 1

die10: Die = Die(10)
print("10 rolls 10 sides:\n")
i = 0
while i < 10:
    die10.roll_die()
    print("---")
    i += 1

die20: Die = Die(20)
print("10 rolls 20 sides:\n")
i = 0
while i < 10:
    die20.roll_die()
    print("---")
    i += 1
print("---------------------------------------")

"""
9-14. Lottery: Make a list or tuple containing a series of 10 numbers 
and 5 letters. Randomly select 4 numbers or letters from the list and 
print a message saying that any ticket matching these 4 numbers or 
letters wins a prize.
"""
from random import choice
print("\n LOTTERIA\n")

lottery: list = [1,2,3,4,5,6,7,8,9,10,"a","b","c","d","e"]
winner_list : list = []
conta: int = 0
while conta <= 4:
    (winner_list.append(choice(lottery)))
    conta += 1
print(winner_list)

print(f"The winning characters are:\n")
for i in winner_list:
    print(f"{i},\n")

print(f"Here's the full ticket : {winner_list}")

print("---------------------------------------")

"""
9-15. Lottery Analysis: You can use a loop to see how hard it might be 
to win the kind of lottery you just modeled. Make a list or tuple 
called my_ticket. Write a loop that keeps pulling numbers until 
your ticket wins. Print a message reporting how many times the 
loop had to run to give you a winning ticket.
"""

my_ticket : list = [4,2,"b",5,"d"]

winning_list : list = []

contatore : int = 0

while my_ticket != winning_list:
    winning_list.append(choice(lottery))
    if len(winning_list) > 5:
        winning_list.clear()
        contatore += 1

print(winning_list)

print(f"Hai vinto! La lotteria è stata estratta {contatore} volte")
    









        

