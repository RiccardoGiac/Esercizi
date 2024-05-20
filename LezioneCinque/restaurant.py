#Riccardo Giacalone
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