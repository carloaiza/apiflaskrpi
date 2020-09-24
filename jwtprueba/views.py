from flask_jwt import jwt_required
from jwtprueba import app
from jwtprueba.EmulatorGUI import GPIO
from flask import request



LEDS = {"green": 16, "red": 18}
#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDS["green"], GPIO.OUT)
GPIO.setup(LEDS["red"], GPIO.OUT)


@app.route('/')
def inicio():
    return 'Bienvenidos a profundización 2'


@app.route('/saludo')
@jwt_required()
def saludo():
    return 'Hola campeones'


@app.route('/led/<color>/', methods=["GET", "POST"])
@jwt_required()
def api_leds_control(color):
    print(request.data)
    print(type(request.data))
    
    if request.method == "POST":
        if color in LEDS:
            #GPIO.output(18,True)
            GPIO.output(LEDS[color], int(request.data.get("state")))       
    
    return {color: GPIO.getStatePinOut(LEDS[color])}
