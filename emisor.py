import random
import socket
from bitarray import bitarray
#Este es el cliente, se encarga de conectar con el servidor. Se encarga de enviar los datos.  

HOST_IP = "127.0.0.1"       
PORT = 60000                #Puerto de envio
bArray = bitarray('10011')

def noiseFunction(bArray):
    
    randomPosition = random.randrange(0,len(bArray),1)
    randomElement = random.randrange(0,1,1)

    print(bArray)
    print("Posicion al azar dentro del array ", randomPosition)
    print("Elemento que reemplazara en el array", randomElement)
    #for n in bArray:
    bArray[randomPosition] =  randomElement
    print(bArray)
    return (bArray)
    


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #Se conecta con el servidor (receptor)
    s.connect((HOST_IP, PORT))
    noiseFunction(bArray)
    #Se envia el mensaje, hola mundo como prueba de envio
    s.sendall(bArray)

    #El receptor envió el "hola mundo" de vuelta
    data = s.recv(1024)


print("Recibido y lo que se envió es:", repr(data))

