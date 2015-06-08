#Autores:#
* Braulio Pareja Manzanares
* Carlos Campos Fe
* Juan Francisco García Pereira
* Luis Miguel Páez Molina
* Jose Antonio Muñoz Fuentes

#Introducción:#
Hemos realizado un programa que consiste en compartir una carpeta entre un servidor y varios
clientes de modo que los clientes tendrán accesos local en su equipo a todos los archivos del
servidor y viceversa, así se actualizaran todos los archivos para que estén en las dos carpetas.
Hemos utilizado Zeromq para la conexión entre los equipos y la transferencia de ficheros.

#¿Como se usa?#
Se ejecuta el archivo servidor.py en el servidor para que este activo, y en el cliente se
ejecuta el archivo cliente.py seguido de la ip a la que queremos sincronizar para empezar a
sincronizar las carpetas, si se deja ejecutándose se actualizara la carpeta del cliente cada diez
segundos para así tenerla actualizada constantemente.
