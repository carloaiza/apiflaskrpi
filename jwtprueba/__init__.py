from flask import Flask
from jwtprueba.database import init_db, shutdown_db_session

app = Flask(__name__)

import jwtprueba.jwt
import jwtprueba.views


init_db()

@app.teardown_appcontext
def shutdown_session(exception=None):
    shutdown_db_session()