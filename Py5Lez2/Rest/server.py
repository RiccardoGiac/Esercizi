from flask import Flask, json, request
from myjson import JsonDeserialize, JsonSerialize

sFileAnagrafe = "./anagrafe.json"
api = Flask(__name__)

@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    #prendi i dati della richiesta
    content_type = request.headers.get('Content-Type') 
    print("Ricevuta chiamata " + content_type)
    if content_type =="application/json": #se il pacchetto che arriva al server è tipo json fa sta roba
        jRequest = request.json #request.json è il pacchetto di risposte che dà il cittadino da client.py in formato json(chiave il cod fis con valori simile dizionario)
        sCodiceFiscale = jRequest["codice fiscale"] #del pacchetto risposte ci interessa il cod fiscale
        print("Ricevuto " + sCodiceFiscale)
        #carichiamo l'anagrafe
        dAnagrafe = JsonDeserialize(sFileAnagrafe) #trasformiamo il json in dizionario python
        if sCodiceFiscale not in dAnagrafe: #se nel dizionario non c'è codice fiscale che corrisponde a quello del pacchetto risposte
            dAnagrafe[sCodiceFiscale] = jRequest #si crea una nuova chiave col nuovo codice fiscale con i valori del pacchetto risposte del cittadino
            JsonSerialize(dAnagrafe, sFileAnagrafe) #il dizionario modificato si ritrasforma in json
            jResponse = {"Error":"000", "Msg": "ok"}# la procedura termina correttamente
            return json.dumps(jResponse), 200
        else:
            jResponse = {"Error":"001", "Msg": "codice fiscale gia presente"} #se il codice fiscale del pacchetto risposte del cittadino è già presente nel dizionario da errore
            return json.dumps(jResponse), 200
    else:
        return "Errore, formato non riconosciuto", 401
    
@api.route('/req_cittadino', methods=['POST'])
def GestisciReqCittadino():
    content_type = request.headers.get('Content-Type') 
    print("Ricevuta chiamata " + content_type)
    if content_type =="application/json":
        jRequest = request.json
        sCodiceFiscale = jRequest["codice fiscale"]
        dAnagrafe = JsonDeserialize(sFileAnagrafe)
        if sCodiceFiscale in dAnagrafe:
           # print(f"Ecco i dati richiesti: {dAnagrafe[sCodiceFiscale]}")
            jResponse = {"Error":"000", "Msg": f"Ecco i dati richiesti: {dAnagrafe[sCodiceFiscale]}"}
            
            return json.dumps(jResponse), 200
            
        else:
            jResponse = {"Error":"001", "Msg": "codice fiscale non riconosciuto"}
            return json.dumps(jResponse), 200

    else:
        return "Errore, formato non riconosciuto", 401

@api.route('/mod_cittadino', methods=['POST'])
def ModificaCittadino():
    newdict = {}
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if content_type =="application/json":
        jRequest = request.json
        sCodiceFiscale = jRequest["codice fiscale"]
        dAnagrafe = JsonDeserialize(sFileAnagrafe)
        if sCodiceFiscale in dAnagrafe:
            mod = input("Inserisci nuovo nome: ")
            newdict["nome"] = mod
            mod = input("Inserisci nuovo cognome: ")
            newdict["cognome"] = mod
            mod = input("Inserisci nuova data nascita: ")
            newdict["data nascita"] = mod
            newdict["codice fiscale"] = sCodiceFiscale
            dAnagrafe[sCodiceFiscale] = newdict
            jResponse = {"Error":"001", "Msg": "ok"}
            return json.dumps(jResponse),200
        else:
            jResponse = {"Error":"001", "Msg": "codice fiscale non riconosciuto"}
            return json.dumps(jResponse), 200
    else:
        return "Errore, formato non riconosciuto", 401

api.run(host="127.0.0.1", port=8080)

