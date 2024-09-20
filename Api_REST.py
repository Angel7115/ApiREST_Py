from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta para manejar GET request
@app.route('/saludo', methods=['GET'])
def saludo_get():
    return jsonify({'mensaje': '¡Hola, este es un saludo desde GET!'})

# Ruta para manejar POST request
@app.route('/saludo', methods=['POST'])
def saludo_post():
    return jsonify({'mensaje': '¡Hola, este es un saludo desde POST!'})

# Ruta para manejar PUT request
@app.route('/saludo', methods=['PUT'])
def saludo_put():
    return jsonify({'mensaje': '¡Hola, este es un saludo desde PUT!'})

# Ruta para manejar DELETE request
@app.route('/saludo', methods=['DELETE'])
def saludo_delete():
    return jsonify({'mensaje': '¡Hola, este es un saludo desde DELETE!'})

if __name__ == '__main__':
    app.run(debug=True)
