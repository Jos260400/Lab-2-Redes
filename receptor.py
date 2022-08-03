from matplotlib import pyplot as plt
import numpy as np
import socket

HOST = "127.0.0.1"
PORT = 60000

#def fletcherCheckSum(bArray):


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))

    s.listen()

    connection, address = s.accept()

    with connection:
        print(f"Connectado a {address}:")
        
        #Se queda esperando hasta recibir los datos del emisor
        while True:
            data = connection.recv(1024)
            if not data:
                break

            connection.sendall(data)
            print(data.decode())
            print("El mensaje recibido es:", repr(data))

