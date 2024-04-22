"""
Data una stringa s che contiene parole e spazi, restituire la lunghezza dell'ultima parola in s.
Una parola è una sottostringa che contiene caratteri contigui diversi dallo spazio

Esempio :
s = "Hello World" -> restituire 5    (len di world è 5)
"""

def length_Of_Last_Word(s: str) -> int:
    srev: str = "".join(reversed(s))
    i:int = 0
    curre_len: int = 0
    while i < len(s):
        if s[i] != " ":
            curre_len += 1
        else:
            break
        i += 1
    return curre_len

#oppure

# l: list[str] = s.split()
# return len(l[-1]) 
            


        