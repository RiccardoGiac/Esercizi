#Riccardo Giacalone

"""
Crea un context manager che permette di calcolare il tempo che viene 
impiegato ad eseguire le istruzioni che si trovano nel with

with Timer():

    time.sleep(1)

time elapsed: 1.00000

in questo esempio il tempo passato non sarà mai uguale a 1
"""

class Timer:

    def __enter__(self):
        import time

        self.time = time.time()

    def __exit__(self,exc_type,exc_value,traceback):

        import time
        
        print(f"Time elapsed: {time.time() - self.time}")

        return False
    

with Timer():

    import time

    time.sleep()