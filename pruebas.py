from matplotlib import pyplot as plt
from email import message
import random
import string
import numpy as np
from bitarray import bitarray

randomPosition = random.randrange(0,2,1)
#print(randomPosition)
#bArray = [1,0,0,1]
#bitarray(bArray)
#
bArray = bitarray('01101000 01101111 01101100 01100001')

def checkSum1(message, sections):
    sections = int((len(message))/4)                      
    p1 = message[0:sections]
    p2 = message[sections:2*sections]
    p3 = message[2*sections:3*sections]
    p4 = message[3*sections:4*sections]

    #print(type(p1))
    sum = bin(int(p1.to01(),2) + int(p2.to01(),2) + int(p3.to01(),2) + int(p4.to01(),2))[2:]
    print(p1)
    print(p2)
    print(sum)

checkSum1(bArray, len(bArray))
