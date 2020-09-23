from flask_jwt import jwt_required
from jwtprueba import app


@app.route('/')
def inicio():
    return 'Bienvenidos a profundización 2'


@app.route('/saludo')
@jwt_required()
def saludo():
    return 'Hola campeones'