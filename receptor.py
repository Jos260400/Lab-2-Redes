import socket
import random 
from bitarray import bitarray

HOST = "127.0.0.1"
PORT = 60000

#def fletcherCheckSum(bArray):
bArray = bitarray('01101000 01101111 01101100 01100001')

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
            
            
            bString = str(data.decode())
            res = ''.join(format(ord(i), '08b') for i in bString)
            print(res)
            #res = ''.join(format(ord(i), '08b') for i in data)

            def checkSum2(message, sections):

                sections = int((len(message))/4)                      
                p1 = message[0:sections]
                p2 = message[sections:2*sections]
                p3 = message[2*sections:3*sections]
                p4 = message[3*sections:4*sections]

                sum2 = bin(int(p1,2) + int(p2,2) + int(p3,2) + int(p4,2))[2:]

                print("El resultado del checksum pos-ruido es:",sum2)


                return sum2


            def checkTotalSum(sum1,sum2):
                if sum1 == sum2:
                    print("Exitoso")

                elif (sum1 != sum2):
                    print("Fallo")

            connection.sendall(data)
            #binaryString = bin(data)
            #print(data.decode())
            checkSum2(bin(int(res,2)), len(bin(int(res,2))))
            checkTotalSum(bArray, bin(int(res,2)))
            print("El mensaje recibido es:", repr(data))


