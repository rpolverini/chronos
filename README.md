# chronos
Alarma Sonora cuando tu laptop alcanza un porcentaje minimo de bateria / Sound alarm when your laptop reaches a minimun percentage of battery

Configuracion basica en las primeras lineas del script: 
archivoTestigo = Nombre de archivo dentro del home del usuario que ejecute el script, donde guardara una instantanea del porcentaje de bateria.
sonido= archivo de alerta sonora (ejemplo debian ... "/usr/share/sounds/gnome/default/alerts/...ogg")
limiteBateria = Porcentaje de bateria minimo, siendo menor a esta la lectura, y no estando conectado, sonara la alarma sonora cuando se ejecute el script



Configuración elemental y necesaria en crontab (gracias  @cgnunezbantics)
# *  *  *  *  * user-name command to be executed each 3 minutes
*/3  *  * * *   rfpolverini	/usr/bin/python3 /home/.../batery.py > /home/../batlog.txt
