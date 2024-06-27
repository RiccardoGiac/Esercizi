#Data una lista e un numero k spostare gli elementi di k posizioni a destra
from LezioneVentuno.lez_ventuno import decorator

@decorator
def rotate_left(l: list[int], k: int) -> list:

    i: int = 0
    while i < k:
        l.append(l.pop(0))
        i += 1
    print(l)
    
rotate_left([1,2,3,4,5],29)
