from flask import Flask, render_template, redirect, url_for,request, session
from flask import json



app = Flask(__name__)#obejto
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
app.config['DEBUG'] = True

usuarios={}
pre =[]
f=open("Usuarios.txt","r")
todo = f.readlines()
f.close
for persona in todo:
	pre = pre + persona.split(":")
i = 0
while i < len(pre):
	usuarios[str(pre[i])] = str(pre[i+1])
	i = i + 2

@app.route('/', methods=['GET', 'POST'])
def login():
	"""
	entrada: username y password
	descripcion: dado un username y una contraseña, verifica que estos esten en el sistema (se hayan registrado) y coincidan, dado el caso los nvía al menu principal, de lo contrario muestra un error
	salida: redireccionar al menu princial
	"""
	global usuarios	
	error = ""
	if request.method == 'POST':
		if request.form["Login"] == "login":
			#iniciar sesion
			if request.form["username"] != "" and request.form["pswd"] != "" and request.form["username"] in usuarios:
				if usuarios.get(str(request.form["username"])) == str(request.form["pswd"]):
					session['usr'] = str(request.form["username"])
					Nombre = session['usr']
					return redirect(url_for('Chat_Menu', Nombre = Nombre))
				else:
					error = "Nombre de Usuario o contrasena incorrectos"
					return render_template("main.html", error = error)
			else: 
				error = "Nombre de Usuario o contrasena incorrectos"
				return render_template("main.html", error = error)
		else: 
			return render_template("main.html", error = error)
	
	return render_template("main.html", error = error)


@app.route('/register', methods =['GET','POST'])
def registrar():
	"""
	entrada: Username y password
	descripcion: el usuario ingresa un username ( que no esté registrado previamente) y una contraseña, el programa lo guarda en un archivo.txt y crea su archivo de soliciudes de amistad y de contactos
	salida: lo redirige a la pagina de login para que pueda inicar sesion.
	"""
	global usuarios
	error = ""	
	if request.method == 'POST':
		#registrarse
		if request.form["Regist"] == "Register":
			if request.form["usernamer"] != "" and request.form["pswdr"] != "" and request.form["confirm"] != "" and request.form["confirm"]==request.form["pswdr"]:
				for persona in usuarios:
					if request.form["usernamer"] == str(persona):
						error = "Nombre de usuario NO disponible"
						return render_template("register.html", error = error)
					else:						
						usuarios[str(request.form["usernamer"])]=str(request.form["pswdr"])						
						f = open("Contactos/"+str(request.form["usernamer"]),"w")
						f.close
						h = open("Solicitudes/"+str(request.form["usernamer"]),"w")
						h.close
						i = open("Usuarios.txt","a")
						i.write(":"+request.form["usernamer"]+":"+request.form["pswdr"])
						i.close
						return redirect(url_for('login'))
			else:
				error = "No ha ingresado datos o las cotrasenas NO coinciden"
				return render_template("register.html", error = error)
		else: 
			return render_template("register.html", error = error)
	
	return render_template("register.html", error = error) #regresar string



@app.route('/menu', methods=['GET','POST'])
def Chat_Menu():
	"""
	descripción: muestra las solicitudes pendiestes del usuario.
	"""
	global usuarios 
	i = open("Solicitudes/"+str(session['usr']),"r")
	pre = []
	pre=i.readlines()
	i.close
	solicitudes = []
	for solicitud in pre:
		solicitudes = solicitudes + solicitud.split("/")
	error=""
	if request.method == 'POST':
		if request.form["buscar"] == "Buscar":
			if str(request.form["agregar"]) in usuarios and str(request.form["agregar"])!="":
				if str(request.form["agregar"]) == session['usr']:
					error = "NO te puedes agregar a ti mismo"
					return render_template('menu.html', error = error)
				else:
					f = open("Solicitudes/"+str(request.form["agregar"]), "a")
					f.write("/"+str(request.form["agregar"]))#persona conectada
					f.close
			else:
				error = "El usuario ingresado NO existe"
				return render_template("menu.html", error = error)
		else:
			return render_template('menu.html')

	return render_template('menu.html', solicitudes = solicitudes) 




if __name__ == '__main__':
	app.run(debug = True)#ejecuta el servidor en el puerto 5000
