"""
Dato un intero col_number, restituire il suo corrispondente titolo di colonna
come su un foglio Excel

Esempio 1:
col_number = 1 -> restituisce "A"
col_number = 26 -> "Z"
col_number = 701 -> "ZY"
"""

def convert_to_title(col_number: int) -> str:
    result: str = ""
    while col_number > 0:
        resto: int = (col_number -1) % 26
        result = chr(resto + ord('A')) + result
        col_number = (col_number -1 ) // 26
    return result

print(convert_to_title(52))