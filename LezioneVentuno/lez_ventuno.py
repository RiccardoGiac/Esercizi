
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

#area_cerchio(1) #-> attenzione perchè se si importa da cartella ad esempio il decorator
                  #questa prova della funzione si esegue nel terminale.  


#keyword yield: serve a far ricordare alla macchina il punto in cui mi trovo
#Esempio:per addestrare una rete neurale si passando data set in banchi da 512 righe di codice
#ogni 512 yield si ricorda di partire dal 513 al prossimo banco


def generatore():

    yield "A"
    yield "B"
    yield "C"

prova_generatore = generatore()
print(next(prova_generatore))
print(next(prova_generatore))
print(next(prova_generatore))


import time
from contextlib import contextmanager

@contextmanager
def timer():
   
    start_time = time.time() #prima dello yield è come se fosse __enter__ di context manager
    yield
    end_time = time.time() #dopo è come se fosse __exit__
    elapsed_time = end_time - start_time
    
    print(f"Elapsed time: {elapsed_time} seconds")  #tutto ciò è fare il context manager senza classe senza enter senza exit
    #solo che è più semplificato e più difficile da capire ciò che rappresenta


#Altro esempio:

@contextmanager

def context_manager_decorator(*args):
    import time

    start_time:float = time.time()
    yield
    end_time:float = time.time()
    elapsed_time:float = end_time - start_time
    print(f"{elapsed_time}")

@context_manager_decorator
def area_cerchio_d(raggio:float):

    return raggio * raggio * 3.14

area_cerchio_d(1)


import sys

a = []
b = a
print(sys.getrefcount(a)) #il numero di volte che faccio riferimento ad a(3)
                          #b anche returna 3 perchè essendo = a si deallocherà
                          # dopo le 3a
                            

threads: list = []

def thread_function(name):

    print(f"{name}Time - {time.time()}")
    time.sleep(2)
    print(f"{name}Time - {time.time()}")

import threading
for i in range (3):  #-> range 3 per 3 threads
    
    x = threading.Thread(target=thread_function,args=(1, )) #args 1 con virgola-> tupla
    threads.append(x)
    x.start()

for t in threads:
    
    t.join()

#print(f"Prima di thread")
#x.start()
#print(f"Thread partito") #-> dopo questo sleep di 2 sec
#x.join() #->aspetta per eseguire il secondo print del time
#print("Thread finito????") #-> printa dopo il secondo time



