
class Room:
#Caricato su moodle
    def __init__(self, id: str, floor: int, seats: int) -> None:
        self.id: str = id
        self.floor: int = floor
        self.seats: int = seats
    
    def get_floor(self):
        return self.floor
    def get_seats(self):
        return self.seats
    def get_id(self):
        return self.id

    def __str__(self) -> str:
        return f"{self.name}"

class Building:
    
    def __init__(self, name :str, address: str,num_floors: int) -> None:
        self.name : str = name
        self.address : str = address
        self.num_floors: int = num_floors
        self.rooms : list[Room] = []

    def get_rooms(self):
        return self.rooms
    
    def get_num_floors(self):
        return self.num_floors
    
    def __str__(self):
        return f"{self.name.capitalize()} @ {self.address}"
    
    def add_room(self, room:Room):
        if room and isinstance(room,Room) and room not in self.rooms\
            and room.get_floor() <= self.get_num_floors():
            self.rooms.append(room)
    
    def __str__(self) -> str:
        s: str = f"{self.name} @ {self.address}\n"
        s+= "With Rooms:\n"
        for room in self.get_rooms():


smi = Building(name = "SMI", address= "Via Sierra Nevada 60", num_floors=5)
armellini = Building(name="ITIS", address="Basilica San Paolo",num_floors=3)
smi.add_room(Room(id="666",floor=3,seats=32))
armellini.add_room(Room(id="333", floor=2, seats=50))
print(smi.get_rooms())
print(armellini.get_rooms())
