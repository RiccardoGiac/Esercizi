#Riccardo Giacalone
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