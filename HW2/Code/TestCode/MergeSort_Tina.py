"""Tina Drew - 035006375
ECE573 - Spring 2018
Homework 2
This Code is to asnwer the Question 3 of homework #2
It generates an array of values and then runs a sorting 
algorithm on them
"""
import os
import math
from test.test_traceback import boundaries
arr = []

arr2 = [1, 20, 30]
arr3 = [4, 5, 6]

class glVar():
    arr = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    directory = myFile = ''
    numComp = 0
     

def getFilePath():
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()
    glVar.directory = filedialog.askdirectory()
        
    file = 'TestResults.txt'
    glVar.myFile = open(os.path.join(glVar.directory, file), "a+" )


def mergeSortStand(arr):
    numComp = 0
            
    #splits main array into two subarrays
    mid = int(len(arr)/2)
    arrL = arr[0:mid]
    arrR = arr[mid:len(arr)]
    
    #sorts right and left subarrays
    arrL, Comp1 = holdSort(arrL)
    arrR, Comp2 = holdSort(arrR)
          
    #sorts merged subarrays
    arr, Comp3 = mergeS(arrL, arrR)
    numComp = Comp1+Comp2+Comp3
    
    print(Comp1)
    print(Comp2)
    #print(arr)
    #print(numComp)
    
    return arr, numComp
    

#holdSort(arr)
#mergeSortStand(arr)

def mergeSortBottomUp(arr):
    Comp1 = Comp2 = Comp3 = sz =  0
    x = 1
    #divides array in or subarrays    
    while sz < int(len(arr)/2+1):
        #increases size by powers of 2
        sz  = 2**x 
        #Sort subarry of size sz
        i = j = 0
        #creates temporary empty array
        a = []
        #breaks up the array 
        for y in range (math.ceil((len(arr)/sz))):
            j += sz
            sub, Comp1 = mergeS(arr[i:j])
            #adds sorted subarry to temporary array
            a.extend(sub)
            #print(a)
            i = j
           
            #sorts additional p that are left offver
            #if j > len(arr):
                #sub, Comp2 = holdSort(arr[i-sz:])
                #del a[i-sz-1:]
                #a.extend(sub)
            glVar.numComp += Comp1
        x += 1
        arr = a
    
    glVar.numComp += Comp2
   
    return arr, glVar.numComp

def mergeS(a):
    arr= []
    numComp = 0
    
    L = a[:int(len(a)/2)]
    #print(L)
    R = a[int(len(a)/2):]
    
    while len(L) > 0 and len(R) > 0:
        if R[0] > L[0]:
            arr.append(L.pop(0))
        else:
            arr.append(R.pop(0))
        numComp += 1
        #print(arr)
    #adds the rest of the array to the test array 
    
    arr = arr + L + R
        
    return arr, numComp

C = [1, 7, 2, 4]
#y, z = mergeS(C)
glVar.arr, z = mergeSortBottomUp(glVar.arr)
print(z) 
print(glVar.arr)
input("Press enter to exit")


