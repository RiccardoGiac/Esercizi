import sys
import os
import os.path
import time

#pip3 install psycopg2-binary
import dbclient as db


print("Inizio programma prova database")
cur = db.connect() #torna un puntatore che si usa quando viene connesso al database
if cur is None:
	print("Errore connessione al DB")
	sys.exit()

sQuery = "select * from anagrafe1" #lettura query sql 
iNumRows = db.read_in_db(cur,sQuery)
for ii in range(0,iNumRows):
	myrow = db.read_next_row(cur)
	print(myrow)

#questo sotto su server.py
sQueryPerReadCodiceFiscale = "select * from anagrafe1 where codice_fiscale ='" +sCodiceFiscaleCittadino + "';"
iNumRows = db.read_in_db(cur,sQueryPerReadCodiceFiscale)
if iNumRows == 0:
	pass
	#print codice fiscale non trovato (response)
else:
	#response 200 trovati i dati della query e li mando al client
	pass