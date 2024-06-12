reader = (open("LezioneQuindici/esempio.txt", encoding="utf-8"))


try:
    reader.readline()
    print("sono nella try")
    raise Exception("Eccezione")

except Exception:

    print("sono nella except")

finally:

    print("sono nella finally")
    reader.close()


#la line 1 si può scrivere anche così(dovrebbe anche chiudere automaticamente il file)

with (open("LezioneQuindici/esempio.txt", encoding="utf-8")) as reader:
    pass

#il with è praticamente questo

class ContextManager:
    
    def __enter__(self):
        print("Ciao sono nell'enter")

        return self
    
    def __exit__(self,exc_type, exc_value, taceback):
       
        if exc_type is not None:
            print("Ecceazione")
        return False
    
    


    
with ContextManager as cm