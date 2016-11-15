from flask import Flask
app = Flask(__name__)
from app import views #Esta linea debe de ir siempre al final para asegurar que todo se importe en el orden adecuado 

###@app.route('/')
#def index():
#	return 'El app funciona'