class RecipeManager:

    def __init__(self) -> None:
        self.list_recipes1: list[dict] = []

    def create_recipe(self,name:str,ingredients:list[str])-> dict[str,list[str]]:
        d: dict = {}

        
        if name not in self.list_recipes1:
            
                d[name] = ingredients
                self.list_recipes1.append(d)
                return d
        else:
                print("Errore, ricetta gia esistente")
       
    def add_ingredient(self,recipe_name:str, ingredient:str):
          
          for d in self.list_recipes1:
                if recipe_name in d and ingredient not in d[recipe_name]:
                      d[recipe_name].append(ingredient)
                      return d
                else:
                      return "Errore"

    def remove_ingredient(self,recipe_name:str, ingredient:str):
          for d in self.list_recipes1:
                if recipe_name in d and ingredient in d[recipe_name]:
                      d[recipe_name].remove(ingredient)
                      return d
                else:
                      return "Errore"
                
    def update_ingredient(self, recipe_name:str, old_ingredient:str,new_ingredient:str):
          for d in self.list_recipes1:
                if recipe_name in d and old_ingredient in d[recipe_name]:
                      index: str = d[recipe_name].index(old_ingredient)
                      d[recipe_name][index] = new_ingredient
                      return d
                else:
                      return "Errore"
                
    def list_recipes(self):
          lis : list[str] = []
          for d in self.list_recipes1:
                for k in d:
                      lis.append(k)
                return lis
          
    def list_ingredients(self, recipe_name:str):
          for d in self.list_recipes1:
                for k,v in d.items():
                      if k == recipe_name:
                            return v

    def search_recipe_by_ingredient(self,ingredient:str):
          for d in self.list_recipes1:
                for v in d.values():
                      if ingredient in v:
                            return d               
        
        
                                                        
    
