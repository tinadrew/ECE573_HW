import math

from cgi import log
N = input("Please enter a value for N: \n")

def getValues(N):
    y = int(N)
    x1 = 10*y*math.log10(y)
    x2 = 2*y^2
    print (x1)
    print (x2)
    print("\n")
    #print (x2)


while N != 'e':
    input(N)
    getValues(N)
    #print(int(N)*2)


    