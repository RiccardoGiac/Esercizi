
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

    def wrapper():

        import time
        start = time.time() #in questo modo calcola il tempo per eseguire
                            #la funzione func
        func()

        print(f"Time elapsed: {time.time() - start}")

    return wrapper

