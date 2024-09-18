from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/saludo', methods=['GET'])
def saludo():
    # Aquí puedes personalizar el saludo
    return jsonify({'mensaje': '¡ Hola, bienvenido a mi API!'})

if __name__ == '__main__':
    app.run(debug=True)
