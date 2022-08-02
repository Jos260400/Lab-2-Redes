import random
from bitarray import bitarray

randomPosition = random.randrange(0,2,1)
print(randomPosition)
bArray = [1,0,0,1]
bitarray(bArray)

print(type(bArray))