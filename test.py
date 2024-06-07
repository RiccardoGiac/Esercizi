class RecipeManager:

    def __init__(self) -> None:
        self.list_recipes: list[dict] = []

    def create_recipe(self,name:str, ingredients: list[str])-> dict[str:list[str]]:
        dict_recipe: dict[str:list[str]] = {}
        for d in self.list_recipes:
            if dict_recipe[name] not in d.keys():

                dict_recipe[name] = ingredients
                self.list_recipes.append(dict_recipe)
                return dict_recipe
            else:
                print("Errore, ricetta gia esistente")

    def add_ingredient(self, recipe_name:str, ingredient:str):
        for dict in self.list_recipes:
            if recipe_name in dict.keys() and ingredient not in dict.values():
                dict[recipe_name].append(ingredient)
                return dict
            else:
                print("Errore")

    def remove_ingredient(self,recipe_name:str, ingredient: str):
        for dict in self.list_recipes:
            if recipe_name in dict.keys() and ingredient in dict.values():
                dict[recipe_name].remove(ingredient)
                return dict
            else:
                print("Errore")

    def update_ingredient(self, recipe_name:str, old_ingredient:str, new_ingredient:str):
        for dict in self.list_recipes:
            if recipe_name in dict.keys() and old_ingredient in dict.values():
                dict[recipe_name].remove(old_ingredient)
                dict[recipe_name].append(new_ingredient)
                return dict
            else:
                print("Errore")

    def list_recipes(self):
        for dict in self.list_recipes:
            print(f"{dict.keys()}")
    
    def list_ingredients(self, recipe_name:str)->list[str] :
        for dict in self.list_recipes:
            if recipe_name in dict.keys():
                return dict[recipe_name]
            else:
                "Errore"

    def search_recipe_by_ingredient(self,ingredient:str)-> list[dict]:
        ls: list[str] = []
        for dict in self.list_recipes:
            if ingredient in dict.values():
                ls.append(dict)
        return ls


            
    



            



        
    