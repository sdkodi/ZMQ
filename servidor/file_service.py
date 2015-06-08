#!/usr/bin/env python
# -*- coding: utf-8 -*-

import zmq
import os

def server():

    # Utilizamos REP para recibir y enviar
    context = zmq.Context(1)
    sock = context.socket(zmq.REP)
    sock.bind('tcp://*:4548')

    # bucle de espera
    while True:
        # recepcion de nombre fichero
        msg = sock.recv()
        # Verificamos si esta disponible
        if not os.path.isfile(msg):
            sock.send('')
            continue
        # Abrimos el fichero para leer
        fn = open(msg, 'rb')
        stream = True
        # emprzamos a leer para enviar
        while stream:
            # Lectura bit a bit
            stream = fn.read(128)
            if stream:
                # enviamos datos por bloques
                sock.send(stream, zmq.SNDMORE)
            else:
                # contenido vacio terminamos
                sock.send(stream)

