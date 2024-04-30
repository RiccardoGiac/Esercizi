#Riccardo Giacalone
import copy
"""
8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. 
Call the function, and make sure the message displays correctly.
"""
def display_message():
    print("Hello everyone, i'm currently learning about this chapter")
display_message()
print("-------------------------------------")

"""
8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. 
The function should print a message, such as "One of my favorite books is Alice in Wonderland". 
Call the function, making sure to include a book title as an argument in the function call.
"""
def favorite_book(title: str):
    print(f"One of my favorite books is {title}")
favorite_book("Harry Potter")
print("-------------------------------------")

"""
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
The function should print a sentence summarizing the size of the shirt and the message printed on it. 
Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
"""
def make_shirt(size: str, text: str):
    print(f"The shirt will be size {size} and have the text \"{text}\" on it")
make_shirt("Medium","Hello World")
print("-------------------------------------")

"""
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
"""
def make_shirt():
    print("The shirt will be size Large have the text \"I love Python\" on it")
make_shirt()

def make_shirt(size: str):
    print(f"The shirt will be size {size} and have the text \"I love Python\" on it")
make_shirt("Medium")

def make_shirt(size: str, text: str):
    print(f"The shirt will be size {size} and have the text \"{text}\" on it")
make_shirt("Small", "What'up?")
print("-------------------------------------")

"""
8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. 
The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. 
Call your function for three different cities, at least one of which is not in the default country.
"""
def describe_city(city: str, country: str = "England"):
    print(f"{city} is in {country}.")
describe_city("London")
describe_city("Manchester")
describe_city("Rome", "Italy")
print("-------------------------------------")

"""
8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. 
The function should return a string formatted like this: "Santiago, Chile". Call your function with at least three city-country pairs, and print the values that are returned.
"""
def city_country(city: str, country: str) -> str:
    cc: str = city + ", " + country
    return cc
print(city_country("Rome","Italy"))
print("-------------------------------------")

"""
8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. 
The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. 
Use the function to make three dictionaries representing different albums. Print each return value to show that the  dictionaries are storing the album information correctly. 
Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. 
If the calling line includes a value for the number of songs, add that value to the album’s dictionary. 
Make at least one new function call that includes the number of songs on an album.
"""
def make_album(artist: str, album: str, nsongs: int = None) -> dict:
    album: dict = {"Artist": artist, "Album": album}
    if nsongs != None:
        album["Songs number"] = nsongs
    return album

print(make_album("Drake","Take Care"))
print(make_album("Linkin Park","A Thousand Suns",16))
print("-------------------------------------")

"""
8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. 
Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.
"""
#while True:
#    artist = input("Insert artist name: ")
#    album = input("Insert Album title: ")
#    nsongs = input("Insert number of songs:")
#    print(make_album(artist, album, nsongs))
#    quit_request: str = input("Insert yes to quit the program or anything else to insert new data: ")
#    if quit_request.lower().strip() == "yes":
#        break
#print("-------------------------------------")
"""
8-9. Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.
"""
messages: list = ["Hello","How are you?","Good to see you","Have a good day"]
def show_messages(msgs: list):
    for i in msgs:
        print(i)
show_messages(messages)
print("-------------------------------------")
"""
8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. 
Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. 
After calling the function, print both of your lists to make sure the messages were moved correctly.
"""    
messages: list = ["Hello","How are you?","Good to see you","Have a good day"]

sent_messages: list = []
def send_messages(msgs:list):
    for i in msgs:
        print(i)
        sent_messages.append(i)
    msgs.clear()
send_messages(messages)
print(messages)
print(sent_messages)
print("-------------------------------------")
"""
8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. 
After calling the function, print both of your lists to show that the original list has retained its messages.
"""
messages: list = ["Hello","How are you?","Good to see you","Have a good day"]
messagesc: list = copy.copy(sent_messages)
sent_messages: list = []
def send_messages(msgs:list):
    for i in msgs:
        print(i)
        sent_messages.append(i)
    msgs.clear()
send_messages(messagesc)
print(messages)
print(sent_messages)
print(messagesc)
print("-------------------------------------")
"""
8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. 
The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. 
Call the function three times, using a different number of arguments each time.
"""


    