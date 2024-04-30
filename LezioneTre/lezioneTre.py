#Riccardo Giacalone
import copy
"""
4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
• Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. 
For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
• Add a line at the end of your program, outside the for loop, that states how much you like pizza. 
The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
"""
pizzas: list =["Diavola","Quattro Formaggi","Margherita"]
for i in pizzas:
    if i == "Diavola":
        print(f"My favourite pizza is {i}.")
    elif i == "Quattro Formaggi":
        print(f"{i} is my second favourite type of pizza.")
    else:
        print(f"Pizza {i} is a classic and i really like it.")
print("Pizza is one of my favourite food: 8/10")
print("-------------------------------------")

"""
4-2. Animals: Think of at least three different animals that have a common characteristic. 
Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
• Modify your program to print a statement about each animal, such as A dog would make a great pet.
• Add a line at the end of your program, stating what these animals have in common. You could print a sentence, such as Any of these animals would make a great pet!
"""
animals: list = ["lion","bear","fox"]
for i in animals:
    if i == "lion":
        print(f"The {i} is the king of the jungle.")
    elif i == "bear":
        print(f"The {i} likes to eat fish")
    else:
        print(f"What does the {i} say?")
print("They are all wild animals.")
print("-------------------------------------")

"""
4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
"""
for i in range(1,21):
    print(i)
print("-------------------------------------")

"""
4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. 
(If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)
"""
millions: list = [i for i in range(1, 1000001)]
#for i in millions:
#    print(i)
print("-------------------------------------")

"""
4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. 
Also, use the sum() function to see how quickly Python can add a million numbers.
"""
print(min(millions))
print(max(millions))
print(sum(millions))
print("-------------------------------------")

"""
4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.
"""
odds: list = [i for i in range(1, 20, 2)]
for i in odds:
    print(i)
print("-------------------------------------")

"""
4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.
"""
threes: list = [i for i in range(3, 31, 3)]
for i in threes:
    print(i)
print("-------------------------------------")

"""
4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. 
Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.
"""
cubes: list = [i**3 for i in range(1, 11)]                  #Per ogni elemento tra 1 e 11(da 1 a 10) fai elemento al cubo(i**3) e mettilo nella lista cubes
for i in cubes:
    print(i)
print("-------------------------------------")

"""
4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes. --->> Fatto nel 4-8
"""
"""
4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
• Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.
"""
#userò la lista odds:
print(f"The first three items in odds list are: {(odds[0:3])}")
mid: int = len(odds)//2 - 1
print(f"The three middle items in odds list are: {odds[mid:mid+3]}")
print(f"The last three items in odds list are: {(odds[-3::])}")
print("-------------------------------------")

"""
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. 
Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.
"""
friend_pizzas:list = copy.copy(pizzas)
pizzas.append("Marinara")
friend_pizzas.append("Capricciosa")
for i in pizzas:
    print(f"My favorite pizzas are: {pizzas}")
for i in friend_pizzas:
    print(f"My friends favorite pizzas are: {friend_pizzas}")
print(f"{pizzas} \n{friend_pizzas}")
print("-------------------------------------")

"""
4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing, to save space. 
Choose a version of foods.py, and write two for loops to print each list of foods. ---> Dal 4-12 al 4-15 non è chiaro ed il link del 4-14 fa page not found.
"""

"""
5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False.
"""
dog: str = "American Akita"
print("Is dog == 'Akita inu'? I predict False.")
print(dog == "Akita Inu")
print("Is dog == 'American Akita'? I predict True.")
print(dog == "American Akita")

food: str = "Pizza"
print("is food == 'Pasta'? I predict False.")
print(food == "Pasta")
print("is food == 'Pizza'? I predict True.")
print(food == "Pizza")

person: str = "Davide"
print("is person == 'Carlo'? I predict False")
print(person == "Carlo")
print("is food == 'Davide'? I predict True")
print(person == "Davide")

city: str = "Rome"
print("is city == 'Rome'? I predict True")
print(city == "Rome")
print("is city == 'London'? I predict False")
print(city == "London")

social: str = "Instagram"
print("is social == 'X'? I predict False")
print(social == "X")
print("is social == 'Instagram'? I predict True")
print(social == "Instagram")
print("-------------------------------------")

"""
5-2. More Conditional Tests: You don’t have to limit the number of tests you cre-
ate to 10. If you want to try more comparisons, write more tests and add them

to conditional_tests.py. Have at least one True and one False result for each of
the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list
"""
#Equality or inequality strings
string:str = "Ciao"
print(string != "Ciao")
print(string == "Ciao")
#With If
if string == "Ciao":
    print(string)
else:
    print("sbagliato")
if string != "Ciao":
    print(string)
else:
    print("sbagliato")
#With lower()
if string.lower() == "ciao":
    print(string)
else:
    print("sbagliato")
if string.lower() != "ciao":
    print(string)
else:
    print("sbagliato")
#Numerical tests
number: int = 10
if number == 10:
    print(number)
else:
    print("sbagliato")
if number > 5:
    print(number)
else:
    print("sbagliato")
if number < 5:
    print(number)
else:
    print("sbagliato") 
if number >= 8:
    print(number)
else:
    print("sbagliato")
if number <= 8:
    print(number)
else:
    print("sbagliato")
#using and and or:
if number > 5 and number < 20:
    print(number)
else:
    print("sbagliato")
if number < 5 or number > 11:
    print(number)
else:
    print("sbagliato")
#Test if in list:
ls: list[int] = [3,10,22]
if 3 in ls:
    print("3 is in the list")
else:
    print("3 is not in the list")
if 5 in ls:
    print("5 is in the list")
else:
    print("5 is not in the list")
print("-------------------------------------")
"""
5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
• Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
• Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)
"""
alien_color: str = "green"
if alien_color == "green":
    print("+5 points")
if alien_color == "yellow":
    print("+3 points")
if alien_color == "red":
     None
print("-------------------------------------")

"""
5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
• If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
• If the alien’s color isn’t green, print a statement that the player just earned 10 points.
• Write one version of this program that runs the if block and another that runs the else block.
"""
if alien_color == "green":
    print("+5 points")
else:
    print("+10 points")
if alien_color != "green":
    print("+5 points")
else:
    print("+10 points")
print("-------------------------------------")

"""
5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.

• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed for the appropriate color alien.
"""
def alienColor(alien_color:str):
    if alien_color == "green":
        print("Green: +5 points")
    elif alien_color == "yellow":
        print("Yellow: +10 points")
    else:
        print("Red: +15 points")
alienColor(alien_color)
alien_color = "red"
alienColor(alien_color)
alien_color = "yellow"
alienColor(alien_color)
print("-------------------------------------")

"""
5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
• If the person is less than 2 years old, print a message that the person is a baby.
• If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
• If the person is at least 4 years old but less than 13, print a message that the person is a kid.
• If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
• If the person is at least 20 years old but less than 65, print a message that the person is an adult.
• If the person is age 65 or older, print a message that the person is an elder.
"""
age: int = 6
if age < 2:
    print("The person is still a baby")
elif age >= 2 and age < 4:
    print("The person is a toddler")
elif age >= 4 and age < 13:
    print("The person is a kid")
elif age >= 13 and age < 20:
    print("The person is a teenager")
elif age >= 20 and age < 65:
    print("The person is an adult")
else:
    print("The person is an elder")
print("-------------------------------------")

"""
5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits.
• Write five if statements. Each should check whether a certain kind of fruit is in your list. 
If the fruit is in your list, the if block should print a statement, such as You really like Apples!
"""
fruits: list = ["Apple", "Lemon", "Orange"]
if "Apple" in fruits:
    print("I really like apples!")
if "Lemon" in fruits:
    print("I really like lemons!")
if "Orange" in fruits:
    print("I really like oranges!")
if "Watermelon" in fruits:
    print("I really like watermelons!")
if "Pineapple" in fruits:
    print("I really like pineapples!")
print("-------------------------------------")

"""
5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'. 
Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user.
• If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.
"""
usernames: list = ["admin","Riccardo","Luigi","Fabrizio","Fabio"]
for i in usernames:
    if i == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {i}, thank you for logging in again")
print("-------------------------------------")

"""
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct message is printed.
"""
usernames: list = ["admin","Riccardo","Luigi","Fabrizio","Fabio"]
for i in usernames:
    if i == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {i}, thank you for logging in again")
usernames.clear()
if len(usernames) == 0:
    print("We need to find some users!")
print("-------------------------------------")

"""
5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
• Make a list of five or more usernames called current_users.
• Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
• Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. 
If a username has not been used, print a message saying that the username is available.
• Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. 
(To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)
"""
current_users: list = ["Riccardo", "Fabrizio", "Fabio", "Luigi", "Roberto"]
new_users: list = ["Riccardo", "Mario", "Carlo", "Andrea", "Fabio"]

current_users_lower: list = [i.lower() for i in current_users]

for i in new_users:
    if i.lower() in current_users_lower:
        print("Username has already been used. Please enter a new username.")
    else:
        print("Username available.")
print("-------------------------------------")

"""
5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
• Store the numbers 1 through 9 in a list.
• Loop through the list.
• Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. 
Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.
"""
numbers: list = [i for i in range(1,10)]
for i in numbers:
    if i == 1:
        print(f"{i}st")
    elif i == 2:
        print(f"{i}nd")
    elif i == 3:
        print(f"{i}rd")
    else:
        print(f"{i}th")   
    