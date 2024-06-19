#Riccardo Giacalone

"""
Crea un context manager usando una classe

Definisci una classe FileManager che implementa un context manager che 
gestisce le risorse dei file.

Implementa appropriatamente la funzione __init__, __enter__ e la 
funzione  __exit__

Esempio di funzionamento:

Il context manager deve permettere di aprire il file, 
effettuare operazioni e chiudere la risorsa aperta.

with FileManager('example.txt', 'w') as f:

    f.write('Hello, world!')
"""

class FileManager:

    def __init__(self,file,mode) -> None:
        self.file = file
        self.mode = mode

    def __enter__(self):

        print("Opening file...")
        
        self.file_wrapper = open(self.file,self.mode)

        return self.file_wrapper

    def __exit__(self,exc_type,exc_value,traceback):

        self.file_wrapper.close()


with FileManager(file= "prova.txt",mode="w") as file:

    file.write("Ciao")

#Si può scrivere anche con with open(sotto) ma la differenza è che sotto lo
#mette a disposizione python ma sopra la classe l'abbiamo scritta noi

with open(file="prova.txt",mode="w") as file:

    file.write("Ciao")



        
