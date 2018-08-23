Cliente web que envía la información de potencia en porcentaje por WebSocket.

No es necesario un servidor web y no es necesario que esté en la raspberry, pero requiere que se ejecute en un dispositivo que esté en la misma red local.

Es necesario editar la linea `websocket1 = new WebSocket("ws://192.168.0.101:8765");` con la direccion ip de la Raspberry Pi.