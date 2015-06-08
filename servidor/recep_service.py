#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from socket import socket, error
def escucha():
	
	s = socket()
	# Escuchar peticiones en el puerto 4547.
	s.bind(('', 4547))
	while True:
	    s.listen(0)
	    conn, addr = s.accept()
	    path = conn.recv(1024)
	    dest = open("f1/"+path, 'w+')
	    while True:
		try:
		        # Recibir datos del cliente.
		    
			input_data = conn.recv(1024)
		except error:
		    print("Error de lectura.")
		    break
		else:
		    if input_data:
		            # Almacenar datos.
			dest.write(input_data)
		    else:
		            break
	    print("El archivo se ha recibido correctamente.")
	    dest.close()


