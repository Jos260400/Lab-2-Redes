from matplotlib import pyplot as plt
import random
import socket
import numpy as np
from bitarray import bitarray
#Este es el cliente, se encarga de conectar con el servidor. Se encarga de enviar los datos.  

HOST_IP = "127.0.0.1"       
PORT = 60000                #Puerto de envio
bArray = bitarray('01101000 01101111 01101100 01100001')

def checkSum1(message, sections):
    sections = int((len(message))/4)                      
    p1 = message[0:sections]
    p2 = message[sections:2*sections]
    p3 = message[2*sections:3*sections]
    p4 = message[3*sections:4*sections]

    #print(type(p1))
    sum1 = bin(int(p1.to01(),2) + int(p2.to01(),2) + int(p3.to01(),2) + int(p4.to01(),2))[2:]
    print("El resultado del checksum pre-ruido es:",sum1)
    

    
    return sum1


def checkSum2(message, sections):
    
    sections = int((len(message))/4)                      
    p1 = message[0:sections]
    p2 = message[sections:2*sections]
    p3 = message[2*sections:3*sections]
    p4 = message[3*sections:4*sections]

    sum2 = bin(int(p1.to01(),2) + int(p2.to01(),2) + int(p3.to01(),2) + int(p4.to01(),2))[2:]

    print("El resultado del checksum pos-ruido es:",sum2)
    return sum2




def noiseFunction(bArray):
    
    randomPosition = random.randrange(0,len(bArray),1)
    randomElement = random.randrange(0,1,1)

    #print(bArray)
    #print("Posicion al azar dentro del array ", randomPosition)
    #print("Elemento que reemplazara en el array", randomElement)
    #for n in bArray:

    bArray[randomPosition] =  randomElement

    #print(bArray)
    
    return (bArray)
    

def checkTotalSum(sum1,sum2):
    if sum1 == sum2:
        print("Exitoso")

    elif (sum1 != sum2):
        print("Fallo")
    
    

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #Se conecta con el servidor (receptor)
    s.connect((HOST_IP, PORT))
    
    sum1 = checkSum1(bArray, len(bArray))
    noiseFunction(bArray)
    sum2 = checkSum2(bArray, len(bArray))
    
    checkTotalSum(sum1, sum2)

    #Se envia el mensaje, hola mundo como prueba de envio
    s.sendall(bArray)

    #El receptor envió el "hola mundo" de vuelta
    data = s.recv(1024)


print("Recibido y lo que se envió es:", repr(data))

