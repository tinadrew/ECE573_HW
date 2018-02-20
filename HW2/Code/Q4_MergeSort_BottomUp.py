"""Tina Drew - 035006375
ECE573 - Spring 2018
Homework 2
This Code is to asnwer the Question 3 of homework #2
It generates an array of values and then runs a sorting 
algorithm on them
"""
import os
import math

arr = []

arr2 = [1, 20, 30]
arr3 = [4, 5, 6]

class glVar():
    #arr = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    dataFiles = ''
    currFile = ''
    dataArr = []
    dataSum = []
    dataSorted = []
    directory = ""
    shellCompPh = 0
    insCompPh = 0
    shellCompTot = 0
    myFile = ''
    directory = myFile = ''
    numComp = 0
   
#The code below opens and dialog box and allows the user to select a 
#directory 
def getFilePath():
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()
    glVar.dataFiles = filedialog.askopenfilenames(parent=root,title='Select files to be tested')
    glVar.directory = os.path.dirname(glVar.dataFiles[0])
    
    file = 'TestResults_Q4_MergeSort_BottomUp.txt'
    glVar.myFile = open(os.path.join(glVar.directory, file), "a+" )

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
                
        print("Number of comparision for insertion sort comparisons: ", glVar.numComp)
    
    glVar.dataSorted = arr


    #sets data array to summary of elements
    glVar.dataSum.extend((glVar.currFile, glVar.numComp))
   
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

def writeDataFile():
    #write header information to file
    header = ['Datafile', 'NumComp']
    glVar.myFile.write('\n') 
    glVar.myFile.write(str(header))
    glVar.myFile.write('\n')           
    glVar.myFile.write(str(glVar.dataSum))
    glVar.myFile.write('\nSorted array: \n')
    glVar.myFile.write(str(glVar.dataSorted))
    glVar.myFile.write('\n')
    

def runMergeSortBot():  
    for f in glVar.dataFiles:
        glVar.dataSum = []
        glVar.currFile = os.path.basename(f)
        with open(f) as fi:
            data1 = fi.read().splitlines()
            glVar.dataArr = [int(x) for x in data1]
                #print(data)
        #print(glVar.dataArr)
        mergeSortBottomUp(glVar.dataArr)
        writeDataFile()


getFilePath()
outputArray = input('Would you like to output the array to the screen?  Enter "Y" for yes and "N" for no: \n')

#print(glVar.dataArr)
runMergeSortBot()
print('After you exit the program, data can be reviewed in the data file here: ')
print(glVar.myFile)
input('Press enter to exit. \n')



