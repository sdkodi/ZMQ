#!/usr/bin/python2
# -*- coding: utf-8 -*-
import time
import zmq 
import os
import sys
import json
from socket import socket

global dirip 	#variable global que guarda la direccion ip del servidor

#Funcion que comprueba si el parametro recibido es una direccion IP
def validate_ip(s):
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True

#Se comprueba si se han introducido parametros por linea de comando
if(len(sys.argv) > 1):
    dirip=sys.argv[1] #Se asigna el parametro recibido por linea de comando a la variable global que dirip
    if not validate_ip(dirip): #Se llama a la funcion validate_ip para comprobar que el parametro recibido corresponde con una direccion IP
	print "Ip no válida"
	sys.exit() #Finaliza la ejecucion del programa
else:
    print "Introduce la direccion IP del servidor"
    sys.exit()	#Finaliza la ejecucion del programa

#Funcion que obtiene un archivo del servidor a partir del nombre del fichero    
def get_file(path):
    global dirip
    # Open up the file we are going to write to
    dest = open("f1/"+os.path.basename(path), 'w+')
    # Set up the zeromq context and socket
    context = zmq.Context()
    socket = context.socket(zmq.REQ)

    socket.connect('tcp://'+dirip+':4548')
    # send the desired file to the server
    socket.send(path)

    while True:
        # Start grabing data
        data = socket.recv()
        # Write the chunk to the file
        dest.write(data)
        if not socket.getsockopt(zmq.RCVMORE):
            # If there is not more data to send, then break
            break

#Funcion que envia un fichero al servidor a partir del nombre
def put_file(path):
	global dirip
	s = socket()
	s.connect((dirip, 4547)) # conexion con el servidor por el puerto 4547
	s.send(path) #Se envia el nombre del fichero al servidor

	while True:
		f = open("./f1/"+path, "rb")
		content = f.read()
		while content:
		# Enviar contenido.
			s.send(content)
			content = f.read()
		break

	s.close() #cierre de conexion
	f.close() #cierre de fichero
	print("Sincronizacion finalizada")

#Funcion principal que se encarga de sincronizar los ficheros
def ficheros():
	
	global dirip
	context = zmq.Context()
	
	print "Conectando con el servidor"
	socket = context.socket(zmq.REQ)
	socket.connect("tcp://"+dirip+":4546") # conexion con el servidor por el puerto 4546

	socket.send("...")
	message = socket.recv() # se recibe la lista de ficheros que se encuentran en el servidor 
	socket.send("...")
	message = socket.recv() # se realiza una segunda vez para que se actualize la lista por si se añade algun archivo

	data= json.loads(message) #se guarda la lista de ficheros contenida en un json en una lista
	
	#se recorre la lista
	for result in data:
		 
		if not os.path.exists("./f1/"+result): #se comprueban si los ficheros existen en el directorio f1 si no existen se añaden
		
			print "Sincronizando..."
			
			get_file(str(result)) # se llama a la funcion get_file para obtener los ficheros que faltan en nuestro directori f1

	
	
	dirs = os.listdir( "./f1/" ) #se obtiene la lista de ficheros contenidos en nuestro directorio f1
 	#se recorre la lista
 	for result in dirs:
	        if not result in data: #se comprueba si los ficheros de nuestro directorio f1 se encuntran en el servidor y si no se encuentran de añaden
			print "Sincronizando con el servidor"
 	         	put_file(str(result)) #se llama a la funcion put_file para añadir al servidor los ficheros que le faltan
			
 		

if __name__ == '__main__':
	#bucle que se encarga de que cada 10 segundos se sincronizen los ficheros
    while True:
    	ficheros()
    	time.sleep(10)
	

