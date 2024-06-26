#Riccardo Giacalone 18/04/24

print("hello world")

"""
2-3. Personal Message: Use a variable to represent a person’s name, and print a message 
to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”
"""

name: str = "Riccardo"
message: str = f"Hello {name}, would you like to learn some Python today?"
print(message)
print("-------------------------------")

"""
2-4. Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.
"""
name: str = "Mario"
name_upper: str = name.upper()
name_lower: str = name.lower()
print(f"{name}, {name_upper}, {name_lower}")
print("-------------------------------")

"""
2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author.
Your output should look something like the following, including the quotation marks:
Albert Einstein once said, “A person who never made a mistake never tried anything new.”
"""
famous_person: str = "Sebastian Vettel"
quote: str = "Everyone is a Ferrari fan. Even if they say they're not, they are Ferrari fans."
print(f"{famous_person} once said, \"{quote}\"")
print("-------------------------------")

"""2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). 
Assign the value 'python_notes.txt' to a variable called filename. 
Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.
"""
filename: str = "python_notes.txt"
filename: str = filename.removesuffix(".txt")
print(filename)
print("-------------------------------")


"""
3-1. Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.
"""
names: list =["Marco", "Luca", "Giovanni"]
for name in names:
    print(name)
print("-------------------------------")

"""
3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them.
The text of each message should be the same, but each message should be personalized with the person’s name.
"""
for name in names:
    print(f"Buongiorno {name}. Benvenuto nel mio programma.")
print("-------------------------------")

"""
3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples.
Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”
"""
mot: list = ["car","train","yacht"]
for item in mot:
    print(f"I wonder if flying {item}s will ever exist.")
    print(f"Let's take a {item} to go as far as possible.")
print("-------------------------------")

"""
3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner.
Then use your list to print a message to each person, inviting them to dinner.
"""
invlist: list = ["me", "myself", "meAgain"]
for item in invlist:
    print(f"Hello {item}, you are invited to a special dinner!" )
print("-------------------------------")

"""
3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations.
You’ll have to think of someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in your list.
"""
invlist: list = ["Me", "Myself", "I"]
for item in invlist:
    print(f"Hello {item}, you are invited to a special dinner!" )
print(f"What? {invlist[2]} can't have dinner with me today? I'll invite someone else...")
invlist[2] = "AlsoMe"
for item in invlist:
    print(f"Hello {item}, you are invited to a special dinner!" )
print("-------------------------------")

"""
3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
"""
invlist: list = ["Me", "Myself", "I"]
for item in invlist:
    print(f"Hello {item}, you are invited to a special dinner!" )
print(f"What? {invlist[2]} can't have dinner with me today? I'll invite someone else...")
invlist[2] = "AlsoMe"
for item in invlist:
    print(f"Hello {item}, you are invited to a special dinner!" )
print("Hello everyone i found a bigger table so i'll invite three more people")  
invlist.insert(0,"ObviouslyMe")                                                     #Aggiunge item al primo index
invlist.append("OfCourseMe")                                                        #Aggiunge item all'ultimo index
if len(invlist) % 2 == 0:                                                           #Aggiunge item a metà lista
    invlist.insert((len(invlist))//2, "DefinitelyMe")
else:
    invlist.insert((len(invlist)-1)//2, "DefinitelyMe")                             #Se è un odd number si può fare anche senza -1(?) quindi fare la cosa sia per odd che even senza if
#list = [0,1,2,3]
#len(list)-1 = 3		3//2 = 1    -> [0,x,1,2,3]  sbagliato
#len(list)=4             4//2 = 2    -> [0,1,x,2,3] corretto

#list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
#len(list)-1 = 14        14//2 = 7   -> [0,1,2,3,4,5,6,x,7,8,9,10,11,12,13,14] corretto
#len(list)=15            15//2 = 7   -> [0,1,2,3,4,5,6,x,7,8,9,10,11,12,13,14] corretto
for item in invlist:                                                                
    print(f"Hello {item}, you are invited to a special dinner!" )
print(invlist)
print("-------------------------------")

"""
3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list. 
Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
"""
invlist: list = ["Me", "Myself", "I"]
for item in invlist:
    print(f"Hello {item}, you are invited to a special dinner!" )
print(f"What? {invlist[2]} can't have dinner with me today? I'll invite someone else...")
invlist[2] = "AlsoMe"
for item in invlist:
    print(f"Hello {item}, you are invited to a special dinner!" )
print("Hello everyone i found a bigger table so i'll invite three more people")  
invlist.insert(0,"ObviouslyMe")                                                     #Aggiunge item al primo index
invlist.append("OfCourseMe")                                                        #Aggiunge item all'ultimo index
if len(invlist) % 2 == 0:                                                           #Aggiunge item a metà lista
    invlist.insert((len(invlist))//2, "DefinitelyMe")
else:
    invlist.insert((len(invlist)-1)//2, "DefinitelyMe")
for item in invlist:                                                                
    print(f"Hello {item}, you are invited to a special dinner!" )
print(invlist)
print("I'm sorry the new table won't arrive in time for dinner and we have space only for two guests, so i need to organize the list again.")
                                                                                                    #  len(invlist)=6  pop(indice)
while len(invlist) > 2:                                                                             #while 6 > 2 quindi finchè ci sono almeno 2 items in invlist
    print(f"Unfortunately {invlist.pop(0)} you will be removed due lack of space.")                 #rimuovi quello all'indice 0 per fare la lista da 2 items 
                                                                                                    #la condizione per uscire dal while è determinata dal pop degli item
                                                                                                    #che al tempo stesso ne ha salvato il nome che viene utilizzato per print
for i in invlist:
    print(f"{i}, you are still invited!")
for i in range(len(invlist)):                                                                       #len(invlist) = 2 quindi fai questo due volte -> range(2)
    del(invlist[0])                                                                                 #elimina l'item di indice 0    
print(invlist)    
print("-------------------------------")
"""
3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse-alphabetical order.
Print the list to show that its order has changed.
"""
places: list = ["Japan", "America", "Iceland", "England", "Spain"]
sorted(places)
print(places)
print(f"{sorted(places)}")
print(places)
print(f"{sorted(places, reverse = True)}")
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse = True)
print(places)
print("-------------------------------")

"""
3-9. Dinner Guests: Working with one of the programs from Exercises 3, use len() to print a message indicating the number of people you’re inviting to dinner.(3-5.)
"""
invlist: list = ["Me", "Myself", "I"]
for item in invlist:
    print(f"Hello {item}, you are invited to a special dinner!" )
print(f"What? {invlist[2]} can't have dinner with me today? I'll invite someone else...")
invlist[2] = "AlsoMe"
for item in invlist:
    print(f"Hello {item}, you are invited to a special dinner!" )
print(f"{len(invlist)} people have been invited to dinner")
print("-------------------------------")

"""
3-10. Every Function: Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like.
 Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.
"""
food: list = []
food.append("Pizza")
food.insert(0, "Sushi")
if len(food) % 2 == 0:                                                           
    food.insert((len(food))//2, "Carbonara")
else:
    food.insert((len(food)-1)//2, "Carbonara")
print(food)
print(f"{sorted(food)}")
print(food)
food.sort()
print(food)
print(f"{food.pop(2)} will be removed from the list.")
print(food)
print("One more item will be removed from the list")
food.remove("Pizza")
print(food)
print("We don't need this list anymore")
del(food)
print("-------------------------------")

"""
6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live.
 You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.
"""
person: dict = {"first_name" : "Fabrizio", "last_name" : "Barberi", "age" : 29, "city" : "Aprilia" }
print(f"{person['first_name']} {person['last_name']} of age {person['age']} lives in {person['city']} ")
print("-------------------------------")

"""
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary.
Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number.
For even more fun, poll a few friends and get some actual data for your program.
"""
fav_nums: dict = {"Riccardo" : 4, "Fabrizio" : 10, "Andrea" : 3, "Fabio" : 7, "Luigi" : 7}
for key in fav_nums:
    print(f"{key} has {fav_nums[key]} as favorite number.")
print("-------------------------------")

"""
6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
• Print each word and its meaning as neatly formatted output. 
You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. 
Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.
"""
glossary: dict = {"set" : "Unordered collection of items that doesn't have duplicates", "print()" : "Built-in function that prints on the screen what we type in the parenthesis"
                  , "for" : "Structure we usually use to cicle through lists of elements", "int" : "Data type that comprehends Integers numbers",
                  "sorted()" : "Function that returns an ordered list of the list we pass as argument without changing it"}
for key in glossary:
    print(f"{key} : {glossary[key]} \n")
print("-------------------------------")

"""
6-7. People: Start with the program you wrote for Exercise 6-1. Make two new dictionaries representing different people, 
and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.
"""
person: dict = {"first_name" : "Fabrizio", "last_name" : "Barberi", "age" : 29, "city" : "Aprilia" }
person2: dict = {"first_name" : "Riccardo", "last_name" : "Giacalone", "age" : 27, "city" : "Aprilia" }
person3: dict = {"first_name" : "Andrea", "last_name" : "Cogni", "age" : 26, "city" : "Piombino" }

people: list = [person, person2, person3]
for i in range(len(people)):
    for key in people[i]:
        print(f"{key} : {people[i][key]}")
print("-------------------------------")

"""
6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. 
Store these dictionaries in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet. 
"""
pet1: dict = {"type" : "dog" , "owner" : "Paolo"}
pet2: dict = {"type" : "cat" , "owner" : "Carlo"}
pet3: dict = {"type" : "snake" , "owner" : "Diana"}

pets: list = [pet1, pet2, pet3]
for i in range(len(pets)):
    for key in pets[i]:
        print(f"{key} : {pets[i][key]}")
print("-------------------------------")

"""
6-9. Favorite Places: Make a dictionary called favorite_places. 
Think of three names to use as keys in the dictionary, and store one to three favorite places for each person.
To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. 
Loop through the dictionary, and print each person’s name and their favorite places.
"""
favorite_places: dict = {"Fabrizio" : "Spain,France,Greece", "Andrea" : "Japan,Thailand,South Korea", "Luigi" : "America, Iceland"}
for key in favorite_places:
    print(f"{key} likes {favorite_places[key]}")
print("-------------------------------")

"""
6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number. 
Then print each person’s name along with their favorite numbers.
"""
fav_nums: dict = {"Riccardo" : 4, "Fabrizio" : 10, "Andrea" : 3, "Fabio" : 7, "Luigi" : 7}
for key in fav_nums:
    print(f"{key} has {fav_nums[key]} as favorite number.")

fav_nums["Riccardo"] = 4, 22
fav_nums["Fabrizio"] = 10,8
fav_nums["Andrea"] = 3,16,1
fav_nums["Fabio"] = 7,20,15
fav_nums["Luigi"] = 7,11
for key in fav_nums:
    print(f"{key} has {fav_nums[key]} as favorite numbers.")
print("-------------------------------")

"""
6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary.
Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city.
The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.
"""
cities: dict ={"New York" : "", "Tokyo": "", "Prague": ""}
infoNY: dict ={"Country" : "America", "Population": "8,336 millions", "Fact" :
                "More than 800 languages are spoken in New York City,making it the most linguistically diverse city in the world."}
infoT: dict = {"Country" : "Japan", "Population": "13,96 millions", "Fact" :
               "Tokyo holds the record for being the world's most populated metropolis."}
infoP: dict = {"Country": "Czech Republic", "Population" : "1,309 millions", "Fact" : 
               "Prague is home of the largest castle in the world"}
cities["New York"] = infoNY
cities["Tokyo"] = infoT
cities["Prague"] = infoP

for key in cities:
    print(f"{key}: {cities[key]}")
print("-------------------------------")

"""
6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways.
Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program, or improving the formatting of the output.
"""
#changing 6-11

infoM : dict ={"Country" : "Spain", "Population": " 3,223 millions", "Fact" :
               "Madrid has the only monument to the devil in the world." }
cities["Madrid"] = infoM
for key in cities:
    print(f"{(key)}: {cities[key]} \n")
print("Madrid will be removed: \n")
del(cities["Madrid"])
for key in cities:
    print(f"{(key)}: {cities[key]} \n")

infoNY["TimeZone"] = "UTC-5"
infoT["TimeZone"] = "UTC+9"
infoP["TimeZone"] = "UTC+2"
for key in cities:
    print(f"{(key)}: {cities[key]} \n")

