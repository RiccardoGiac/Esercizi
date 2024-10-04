from flask import Flask, jsonify, request
from myjson import JsonDeserialize, JsonSerialize

api = Flask(__name__)


file_path = "anagrafe.json"
cittadini = JsonDeserialize(file_path)
file_path2 = "utenti.json"
utenti = JsonDeserialize(file_path2)

@api.route('/login', methods=['POST'])
def GestisciLogin():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json #contiene la richiesta del client {"username": "mario", "password":"rossi"}
        sUsernameClient = jsonReq["username"]
        sPasswordClient = jsonReq["password"]
        if sUsernameClient in utenti:
            if sPasswordClient == utenti[sUsernameClient]["password"]:
                sPriv = utenti[sUsernameClient]["privilegi"]
                return jsonify({"Esito": "000", "Msg": "Utente registrato", "Privilegio":sPriv}), 200  
            else:
                return jsonify({"Esito": "001", "Msg": "Login errato"}), 200
        else:
            return jsonify({"Esito": "002", "Msg": "Login errato"}), 200
    else:
        return jsonify({"Esito": "003", "Msg": "Formato richiesta non valido"}), 200

@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json
        codice_fiscale = jsonReq.get('codFiscale')
        if codice_fiscale in cittadini:
            return jsonify({"Esito": "001", "Msg": "Cittadino già esistente"}), 200
        else:
            cittadini[codice_fiscale] = jsonReq
            JsonSerialize(cittadini, file_path) 
            return jsonify({"Esito": "000", "Msg": "Cittadino aggiunto con successo"}), 200
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta non valido"}), 200

@api.route('/read_cittadino/<codice_fiscale>', methods=['GET'])#<codice_fiscale> diventa una stringa e la usa come parametro di read_cittadino
def read_cittadino(codice_fiscale):
    cittadino = cittadini.get(codice_fiscale)
    if cittadino:
        return jsonify({"Esito": "000", "Msg": "Cittadino trovato", "Dati": cittadino}), 200
    else:
        return jsonify({"Esito": "001", "Msg": "Cittadino non trovato"}), 200

@api.route('/update_cittadino', methods=['PUT'])
def update_cittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json
        codice_fiscale = jsonReq.get('codFiscale')
        if codice_fiscale in cittadini:
            cittadini[codice_fiscale] = jsonReq
            JsonSerialize(cittadini, file_path)  
            return jsonify({"Esito": "000", "Msg": "Cittadino aggiornato con successo"}), 200
        else:
            return jsonify({"Esito": "001", "Msg": "Cittadino non trovato"}), 200
    else:
        return jsonify({"Esito": "002", "Msg": "Content-Type non supportato!"}), 200

@api.route('/elimina_cittadino', methods=['DELETE'])
def elimina_cittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        cod = request.json.get('codFiscale')
        if cod in cittadini:
            del cittadini[cod]
            JsonSerialize(cittadini, file_path)  
            return jsonify({"Esito": "000", "Msg": "Cittadino rimosso con successo"}), 200
        else:
            return jsonify({"Esito": "001", "Msg": "Cittadino non trovato"}), 200
    else:
        return jsonify({"Esito": "002", "Msg": "Content-Type non supportato!"}), 200

api.run(host="127.0.0.1", port=8080)

