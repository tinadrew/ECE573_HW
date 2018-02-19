"""Tina Drew - 035006375
ECE573 - Spring 2018
Homework 2
This Code is to asnwer the Question 3 of homework #2
It generates an array of values and then runs a sorting 
algorithm on them
"""
import os
import math
arr = [16, 15, 14, 13, 9, 8, 7, 6, 5, 4, 3, 2, 1]

arr2 = [1, 20, 30]
arr3 = [4, 5, 6]

class glVar():
    arr = []
    directory = myFile = ''
     

def getFilePath():
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()
    glVar.directory = filedialog.askdirectory()
        
    file = 'TestResults.txt'
    glVar.myFile = open(os.path.join(glVar.directory, file), "a+" )



def holdSort(arr):
    numComp = 0
    for i in range(1, len(arr)):
        j = i-1
        val =  arr[i]
        
        #updates the number of comparison each time the loop runs
        #numComp += 1
        #Finds proper insertion point for current element item under test
        while j >= 0 and val < arr[j]:
            j -= 1 
            #updates the number of comparison each time the loop runs
            numComp += 1

        if j != i-1:
            #delete a[i] and insert into at position k
            arr.insert(j+1, arr.pop(i))
        #print (arr)
    #print(numComp)
    return arr, numComp

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
    numComp = Comp1 = Comp2 = Comp3 = sz =  0
    x = 1
    a = []
    
    while sz < int(len(arr)/2):
        sz  = 2**x 
        a = []
        #Sort subarry of size sz
        i = j = 0
        
        for y in range (math.ceil((len(arr)/sz))):
            j += sz
            sub, Comp1 = holdSort(arr[i:j])
            a.extend(sub)
            print(a)
            i = j
           
            #sorts additional p that are left offver
            if j > len(arr):
                sub, Comp2 = holdSort(arr[i-sz:])
                del a[i-sz-1:]
                a.extend(sub)
            numComp = Comp1+Comp2
        arr = a
        x += 1
    
    #print('Last Sort array')
    #print(a)    
    arrL = a[:int(len(arr)/2)]
    arrR = a[int(len(arr)/2):]
    arr, Comp3 = mergeS(arrL, arrR)

    
    return arr, numComp
    
def mergeS(L, R):
    arr= []
    numComp = 0
        
    while len(L) > 0 and len(R) > 0:
        if R[0] > L[0]:
            arr.append(L.pop(0))
        else:
            arr.append(R.pop(0))
        numComp += 1
    #adds the rest of the array to the test array 
    arr = arr + L + R
        
    return arr, numComp

y, z = mergeSortBottomUp(arr)
print(y) 
print(z) 
input("Press enter to exit")


