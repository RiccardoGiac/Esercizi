
def ciao(name:str)-> str:

    return f"Ciao, {name}"

def salve(name:str)-> str:
    
    return f"Salve, {name}"

def saluta_bob(func)-> str:

    return func("Bob")  #return ciao("Bob")
                        #In pratica prende in parametro una funzione e le 
                        #da il parametro "Bob"

print(saluta_bob(ciao))
print(saluta_bob(salve))


############

def parent():
    
    print("sono in parent")

    def parent():
        
        print("sono parent dentro parent")

    def first_child():

        print("sono in first_child")
    
    def second_child():

        print("sono in second_child")
    
    second_child()
    second_child()  #non runnano se non si scrive parent() come sotto
    first_child()   #sono visibili solo all'interno di parent
    parent()

parent()

print("############")

def parent():
    
    print("sono in parent")

    def first_child():

        print("sono in first_child")
    
    return first_child

print("#############")

def decorator(func):
   
    def wrapper():
        
        print("prima di func")
        func()
        print("dopo di func")
    
    return wrapper  #senza parentesi se no viene eseguito e ritorna None

def ciao():
    print("ciao")

ciao = decorator(ciao) #modifica la funzione ciao passandola a decorator

ciao() #cosi chiamando ciao printa anche il wrapper (prima e dopo func)

#quindi decorator va a modificare la funzione aggiungendo il wrapper

print("############")

def decorator(func):

    def wrapper(*args):

        import time
        start = time.time() #in questo modo calcola il tempo per eseguire
                            #la funzione func
        func(*args) #args perchè essendo un decorator di funzioni generiche non si sa quanti parametri passare

        print(f"Time elapsed: {time.time() - start}")

    return wrapper #return una funzione senza parentesi returna il riferimento in memoria
                    
@decorator #nome della funzione decorator sopra, in questo modo calcolerà il tempo che la funzione ci metterà ad eseguirsi
def area_cerchio(raggio:float):

    return raggio * raggio * 3.14

class Analisi:

    @staticmethod
    def tempo(func):

        def wrapper(*args):
            
            import time
            start = time.time() 
            func(*args)
            print(f"Time elapsed: {time.time() - start}")
        return wrapper 
        
@Analisi.tempo
def area_cerchio(raggio:float):

    return raggio * raggio * 3.14

#area_cerchio(1)  attenzione perchè se si importa da cartella ad esempio il decorator
                  #questa prova della funzione si esegue nel terminale.  