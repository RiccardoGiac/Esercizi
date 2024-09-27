import json

def SerializzaJson(dData, file_path) ->bool: #dData è un dizionario python
    try:
        with open(file_path, "w") as file:
            json.dump(dData, file)
            print("Operazione riuscita.")
            return True #crea il file json direttamente senza creare la stringa
    except Exception:
            print("Operazione non riuscita.")
            return False  

def DeserializzaJson(file_path) ->dict:
    try:
        with open(file_path, "r") as file:
            print("Operazione Riuscita")
            return json.load(file) #ritorna il json in formato dizionario python
    except Exception:
            print("Operazione non riuscita")


def SerializzaJson1(dData,file_path):
    sData = json.dumps(dData) #crea la stringa da scrivere su file
    try:
        with open(file_path, "w") as file:
            file.write(sData)
        return True
    except Exception:
        return False
    
def DeserializzaJson1(file_path) ->dict:
    sData = ""
    sAppo = ""
    dData = {}
    try:
        with open(file_path, "r") as file:
            sAppo = file.read(500)
            while len(sAppo) == 500:
                 sData += sAppo
                 sAppo = file.read(500)
            if len(sAppo) > 0:
                 sData += sAppo
        if len(sData) > 0:
            dData = json.loads(sData)
            return dData
        else:
             return None
    
    except Exception:
        print("Operazione non riuscita.")


mydict_1 = { "brand": "Ford",
"electric": False,
"year": 1964,
"colors": ["red", "white", "blue"]}

mydict_2 = "{ 'brand':   'Ford'," + \
"'electric': False," + \
"'year': 1964," + \
"'colors': ['red', 'white', 'blue']}"

SerializzaJson(mydict_1, "./mydict.json")
print(DeserializzaJson("./mydict.json"))