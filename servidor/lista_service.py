#!/usr/bin/env python
# -*- coding: utf-8 -*-

import zmq
import time
import os, sys
import json

def lista():
	#ruta de nuestro directorio raiz
	path = "./f1/"
	# Utilizamos REP para recivir y enviar
	context = zmq.Context()
	socket = context.socket(zmq.REP)
	socket.bind("tcp://*:4546")
	
	#obtenemos una lista de ficheros en nuestro path para enviarla
	#como json para que la obtenga el cliete
	while True:
		dirs = os.listdir( path )
		myjson = json.dumps(dirs)
		message = socket.recv()
		time.sleep(1)
		socket.send(myjson)
