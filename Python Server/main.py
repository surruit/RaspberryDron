import asyncio
import websockets
from RPIO import PWM
servo1 = PWM.Servo()

async def updateMotor(websocket, path):
    valor = 0
    while (True):
        #Espera por nuevos datos
        potencia = await websocket.recv()

        #cuando hay un cambio, lo muestra por consola
        print("Potencia: " + potencia + "%")

        #actualiza la potencia del motor
        servo1.set_servo(26, 1000 + int(valor)*10)

start_server = websockets.serve(updateMotor, '0', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
