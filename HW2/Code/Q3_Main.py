"""Tina Drew - 035006375
ECE573 - Spring 2018
Homework 2
This Code is to asnwer the Question 1 of homework #2
It generates an array of va
"""

class glVar():
    arr = []

def genArray():
    a = [1]*1024
    b = [11]*2048
    c = [111]*4096
    d = [1111]*1024
    
    glVar.arr= a+b+c+d
    print (glVar.arr)
    print (len(glVar.arr))
    
    
genArray()