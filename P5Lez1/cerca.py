import os
import PyPDF2

lTextExtensions = [".txt", ".py", ".js", ".csv", ".json", ".css", ".html"]

def cercaStringaInNomefile(sFile,sStringa):
    #mettiamo tutto a minuscolo
    #usiamo sFileLower.find() che torna -1 se la parola non c'è
    #e la posizione della parola altrimenti 
    #torniamo true o false

    #if sStringa.lower() == sFile.lower():
        #print(f"Ho trovato un file con il nome corrispondente alla parola {sStringa}")
        #return True
    #else:
        #print("-1")
        #return False
    sFileLC= sFile.lower()
    sStringaLC = sStringa.lower()

    if(sFileLC.find(sStringaLC)>= 0):
        return True
    else:
        return False

def CercaStringaInTextfile(sFile,sStringa):
    iRet = -1
    with open(sFile, "r") as file1:
        sRiga = file1.readline()
        while len(sRiga) > 0:
            iRet = sRiga.lower().find(sStringa.lower())
            if iRet >= 0:
                return True
            sRiga = file1.readline()
    return False

def CercaStringaInPDFfile(sFile,sString):
	object = PyPDF2.PdfReader(sFile)
	numPages = len(object.pages)
	for i in range(0, numPages):
		pageObj = object.pages[i]
		text = pageObj.extract_text()
		text = text.lower()
		if(text.find(sString)!=-1):
			return True
	return False

                

def cercaStringaInContenutoFile(sPathFile,sStringa):
    
    bRet = False
    sOutFileName,sOutFileExt = os.path.splitext(sPathFile)
    
    if sOutFileExt.lower() in lTextExtensions:
        bRet= CercaStringaInTextfile(sPathFile,sStringa)
    
    if sOutFileExt.lower() == ".pdf":
        bRet= CercaStringaInPDFfile(sPathFile,sStringa)
    
    return bRet
    


sRoot = input("Inserisci directory in cui cercare")
sParola = input("Inserisci parola da cercare")
sOutDir = input("Inserisci directory di output")

iNumFileTrovati = 0
for root, dirs, files in os.walk(sRoot):
    print(f"Sto guardando {root} che contiene {len(dirs)} subdir e {len(files)} file")
    for file in files:
        print(f"Devo vedere se {file} contiene nel nome {sParola}")
        iRet=cercaStringaInNomefile(file,sParola)
        if iRet == True:
            iNumFileTrovati = iNumFileTrovati +1
        else:
            sFilePathCompleto = os.path.join(root,file)
            iRet = cercaStringaInContenutoFile(sFilePathCompleto,sParola)
            if iRet == True:
                iNumFileTrovati += 1
        if iRet == True:
            print("Trovata parola in file" + file)

print(f"Ho trovato {iNumFileTrovati} files")

