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



