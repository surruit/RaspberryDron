# RaspberryDron

Raspberry Pi Zero W como controlador de vuelo.

## Uso ##
Si no lo tienes, instala Python3 y las librerías Websocket y RPIO.

Copia *Python Server/main.py* a la Raspberry Pi

Ejecuta el fichero, si todo está correcto, se verá así:

![ImagenShell-ConexionOK](/Imagenes/ImagenShell-ConexionOK.png)

En este momento, hay un servidor WebSocket esperando un numero del 0 al 100, indicando la potencia en porcentaje.

La señal de salida se genera en el puerto GPIO26. Conectar el puerto GPIO26 de la Raspberry Pi a la entrada de señal del ESC. También es necesario conectar los GND de la Raspberry Pi y el ESC.


En este punto, ya está todo listo, solo es necesario enviarle un numero entre 0 y 100 a la Raspberry Pi por WebSocket.

Abre el archivo *Cliente html/index.html* con un editor de texto y corrige la dirección ip. Abre el archivo con un navegador web, no es necesario un servidor web.

Si todo ha ido bien, en la consola de javascript no debería haber ningún error y el slicer controlará la señal del ESC.

## Licencia ##
![Logo CC0](/Imagenes/CC0.png)