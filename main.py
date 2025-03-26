from flask import Flask, jsonify
import os

app = Flask(__name__)

class Contactos:
    def _init_(self, name, phone):
        self.name = name
        self.phone = phone


@app.route('/')
def index():

    cris = Contactos("Cristian", "5546372819")
    lolita = Contactos("Lolita cortez", "7898675436")
    iron = Contactos("Iron man", "9087965741")
    list[]
    list.append[cris]
    list.append[lolita]
    list.append[iron]
    return jsonify(list)



if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
