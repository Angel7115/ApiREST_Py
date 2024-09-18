from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# URL base de la API MockAPI
MOCKAPI_URL = "https://66eafa8655ad32cda47b3666.mockapi.io/IoTCarStatus"

# Crear (POST) un nuevo registro
@app.route('/carstatus', methods=['POST'])
def create_car_status():
    data = request.json  # Obtenemos los datos del cuerpo de la solicitud
    response = requests.post(MOCKAPI_URL, json=data)  # Hacemos la solicitud POST a MockAPI
    return jsonify(response.json()), response.status_code

# Leer (GET) todos los registros o un registro por ID
@app.route('/carstatus', methods=['GET'])
@app.route('/carstatus/<int:car_id>', methods=['GET'])
def get_car_status(car_id=None):
    if car_id:
        response = requests.get(f"{MOCKAPI_URL}/{car_id}")  # GET por ID
    else:
        response = requests.get(MOCKAPI_URL)  # GET todos los registros
    return jsonify(response.json()), response.status_code

# Actualizar (PUT) un registro existente
@app.route('/carstatus/<int:car_id>', methods=['PUT'])
def update_car_status(car_id):
    data = request.json  # Obtenemos los datos del cuerpo de la solicitud
    response = requests.put(f"{MOCKAPI_URL}/{car_id}", json=data)  # PUT para actualizar
    return jsonify(response.json()), response.status_code

# Eliminar (DELETE) un registro por ID
@app.route('/carstatus/<int:car_id>', methods=['DELETE'])
def delete_car_status(car_id):
    response = requests.delete(f"{MOCKAPI_URL}/{car_id}")  # DELETE por ID
    return jsonify({'message': 'El registro ha sido eliminado'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
