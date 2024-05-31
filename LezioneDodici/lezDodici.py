#assert #Verifica se una condizione è vera

i: int = 0
test_value: int = 0
assert i == 0 #se è vero il codice runna, se no lancia un errore


assert i == test_value, f"Error, i must be {test_value} instead {i}"

def sum(a:int, b:int) -> int:
    return 0

result = sum(a=5,b=2)
test_value: int = 7
assert result == test_value, f"Error, sum must be {test_value} you got {result}"

#all() -> ritorna true se tutto cio' che è nella lista è True
    #esempi all(result)

