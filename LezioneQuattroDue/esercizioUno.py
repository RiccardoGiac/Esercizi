"""
Dato un intero x, restituisci True se x è palindromo, altrimenti False.

Esempio 1
x = 121 -> True
Spiegazione: 121 si legge come 121 sia da destra che sinistra

Esempio 2:
x = -121 -> False
Spiegazione: Da sinistra a destra, leggiamo -121. Da destra a sinistra abbiamo 121- e non è palindromo.
"""

def is_palindrome(x:int) -> bool:
    #xs = str(x)
    #rev = "".join(reversed(xs))  #metodo python
    #return rev == xs

    s:str = str(x)
    i:int = 0
    s_length = len(s)
    while i < (s_length // 2): #for i in range(len(s))     #metodo ragionato java
        j = s_length - (i+1)   # i parte dall'indice 0 mentre j dall'ultimo che effettivamente è len - i+1 
        if s[i] != s[j]:
            return False
        i += 1
    return True


        
    
