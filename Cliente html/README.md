Cliente web que envia la informacion de potencia por WebSocket.

No es necesario un servidor web y no es necesario que este en la raspberry, pero requiere que se ejecute en un dispositivo que este en la misma red local.

Es necesario editar la linea "websocket1 = new WebSocket("ws://192.168.0.101:8765");" con la direccion ip de la Raspberry Pi