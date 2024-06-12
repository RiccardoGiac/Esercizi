#Riccardo Giacalone

class MovieCatalog:
    
    def __init__(self) -> None:
        self.m_dict: dict[str : list[str]] = {}

    def add_movie(self,director_name: str, movies: list[str]):
        self.m_dict[director_name] = movies

    def remove_movie(self,director_name:str,movie_name: str):
        if movie_name in self.m_dict[director_name]:
            self.m_dict[director_name].remove(movie_name)
        if not self.m_dict[director_name]:                 #Se non ha valori rimuove la chiave(regista)
            del self.m_dict[director_name]

    def list_directors(self):
        for k in self.m_dict.keys():
            print(k)

    def get_movies_by_director(self,director_name:str)-> list[str]:
        dir_list: list[str] = []
        for k in self.m_dict:
            if k == director_name:
                for e in self.m_dict[k]:
                    dir_list.append(e)
        return dir_list
    
 ########TESTS#######

mvctlg1: MovieCatalog = MovieCatalog()
mvctlg1.add_movie(director_name="S.Spielberg",movies=["Salvate il soldato Ryan", "Schindler's List"])
mvctlg1.add_movie(director_name="J.Cameron", movies=["Avatar", "Titanic"])
print(mvctlg1.get_movies_by_director("J.Cameron"))
mvctlg1.remove_movie("J.Cameron", movie_name="Avatar")
#mvctlg1.remove_movie("J.Cameron", movie_name="Titanic") -> test per rimuovere la chiave e quindi returnare solo spielberg fra i registi
print(mvctlg1.get_movies_by_director("J.Cameron"))
mvctlg1.list_directors()