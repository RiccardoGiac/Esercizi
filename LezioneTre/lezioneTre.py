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
