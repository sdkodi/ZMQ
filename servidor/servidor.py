#!/usr/bin/env python
# -*- coding: utf-8 -*-

#importamos los ficheros generados para ejecutar con varios hilos a la vez
import file_service
import lista_service
import recep_service
from threading import Thread

def main():
	s1=Thread(target=file_service.server)
	s2=Thread(target=lista_service.lista)
	s3=Thread(target=recep_service.escucha)
	s1.start()
	s2.start()
	s3.start()


if __name__ == '__main__':
    main()
