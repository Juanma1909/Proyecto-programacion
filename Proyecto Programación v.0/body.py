from flask import Flask, render_template, redirect, url_for,request
from flask import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)#obejto
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sql10202466:YfJqpqwrEm@sql10.freemysqlhosting.net/sql10202466'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True

db = SQLAlchemy(app)
class Test(db.Model):
	id = db.Column(db.Integer, primary_key = True)
class Member(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(18),unique = True)



#@app.route('/<name>')
#def Index(name = 'eduardo'):
	#return render_template('main.html',nombre = name)
@app.route('/', methods = ['GET', 'POST'])#decorador
def login():	
	error = None
	if request.method == 'POST':
		if request.form["Login"] == "Login":
			if request.form["username"] != "" and request.form["pswd"] != "" and request.form["username"] in usuarios:
				if usuarios[request.form["username"]] == request.form["pswd"]:
					return render_template("")
				else:
					error = "Nombre de Usuario o contrasena incorrectos"

			else: 
				error = "Nombre de Usuario o contrasena incorrectos"
		else: 
			pass
	else:
		pass


@app.route('/register', methods =['GET','POST'])
def registrar():	
	error = None


	return 'Hola Mundo'#regresar string



if __name__ == '__main__':
	app.run(debug = True)#ejecuta el servidor en el puerto 5000
