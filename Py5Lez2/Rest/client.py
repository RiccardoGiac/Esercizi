import json, requests

base_url = "http://127.0.0.1:8080"

def CreaInterfaccia():
    print("Operazioni disponibili")
    print("1. Inserisci cittadino (es. atto di nascita)")
    print("2. Richiedi dati cittadino (es. cert. residenza)")
    print("3. Modifica dati cittadino")
    print("4. Elimina cittadino")
    print("5. Exit")

def RichiediDatiCittadino():
    nome = input("inserisci nome cittadino: ")
    cognome = input("inserisci cognome cittadino: ")
    dataNascita = input("inserisci data nascita: ")
    codFiscale = input("Inserisci codice fiscale: ")
    jRequest = {"nome":nome, "cognome":cognome,"data nascita": dataNascita,"codice fiscale":codFiscale}
    return jRequest

def RichiediCodF():
    codFiscale = input("inserisci codice fiscale: ")
    jRequest = {"codice fiscale" :codFiscale}
    return jRequest

CreaInterfaccia()
sOper = input("Seleziona operazione")
while sOper != "5":
    if sOper == "1":
        api_url = base_url + "/add_cittadino"
        jsonDataRequest = RichiediDatiCittadino()
        try:
            response = requests.post(api_url,json=jsonDataRequest)
            print(response.status_code)
            print(response.headers["Content-Type"])
            data1 = response.json()
            print(data1)
        except:
            print("Problemi di comunicazione con il server")
    
    if sOper == "2":
        api_url = base_url + "/req_cittadino"
        jsonDataRequest = RichiediCodF()
        try:
            response = requests.post(api_url,json=jsonDataRequest)
            print(response.status_code)
            print(response.headers["Content-Type"])
            data1 = response.json()
            print(data1)
        except:
            print("Problemi di comunicazione con il server")
    
    CreaInterfaccia()
    sOper = input("Seleziona operazione")