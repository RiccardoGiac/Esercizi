from flask import Flask, render_template
from flask import request
api = Flask(__name__)

utenti = [["mario","rossi","mario.1424@gmail.com","1234",0,False],
          ["alessia","garibaldi","alessia.124@yohoo.it","Password01",0,False],
          ["gianni","Gianfranco","gianno.898@gmail.com","2304",0,False]]



@api.route('/', methods=['GET']) #Se l'url è / e metodo è GET manda index
def index():
    return render_template('index.html')


@api.route('/pippo', methods=['GET'])
def index2():
    return render_template('index2.html')

@api.route('/regok', methods=['GET'])
def regok():
    return render_template('reg_ok.html')

@api.route('/regko', methods=['GET'])
def regko():
    return render_template('reg_ko.html')

@api.route('/loginko', methods=['GET'])
def loginko():
    return render_template('login_ko.html')

@api.route('/loginok', methods=['GET'])
def loginok():
    return render_template('login_ok.html')

@api.route('/registrati', methods=['GET'])
def registra():
    nome=request.args.get("nome")
    print("Nome Inserito:"+ nome)

    cognome=request.args.get("cognome")
    print("Cognome inserito:"+cognome)

    email=request.args.get("email")
    print("email inserito:"+email)

    password=request.args.get("password")
    print("Password inserita:"+password)
    l: list[str] =[nome,cognome,email,password,0,False]

    for i in utenti:
        if l==i and i[4] == 0:
            i[4] = 1 #utente registrato (1)
            return render_template('reg_ok.html')
    
    return render_template('reg_ko.html')

@api.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@api.route('/loggati', methods=['GET'])
def loggati():
    email=request.args.get("email")
    

    password=request.args.get("password")
    
    ll: list[str] =[email,password]

    for i in utenti:
        if ll[0] == i[2] and ll[1] == i[3] and i[4] == 1 and i[5] == False:
            i[5] == True #l'utente è già loggato (True) e non può rifare il login
            return render_template('login_ok.html')
    return render_template('login_ko.html')

@api.route('/homee', methods=['GET'])
def homee():
    return render_template('home.html') #devo passa l'utente in html

@api.route('/home', methods=['GET']) 
def home():
    
    return render_template('home.html')
    
@api.route('/logout', methods=['GET'])
def logout():
        for i in utenti:
            if i[5] == True:
                i[5] == False
        return render_template('index.html')


api.run(host="0.0.0.0", port=8085)
