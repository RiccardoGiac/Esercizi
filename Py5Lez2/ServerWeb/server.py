from flask import Flask, render_template

api = Flask(__name__)


@api.route('/', methods=['GET']) #Se l'url è / e metodo è GET manda index
def index():
    return render_template('index.html')

@api.route('/pippo', methods=['GET'])
def index2():
    return render_template('index2.html')

api.run(host="0.0.0.0", port=8085)
