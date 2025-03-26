from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Cristian Cardoso": "+5255352121", "Josue Perez": "+525523145463", "Alfonso Monroy": "+525549692841"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
