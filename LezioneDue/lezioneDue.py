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