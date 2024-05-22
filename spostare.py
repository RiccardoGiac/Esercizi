#Data una lista e un numero k spostare gli elementi di k posizioni a destra

def rotate_left(l: list[int], k: int) -> list:

    i: int = 0
    while i < k:
        l.append(l.pop(0))
        i += 1
    return l
    
print(rotate_left([1,2,3,4,5],29))
