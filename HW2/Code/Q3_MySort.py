"""Tina Drew - 035006375
ECE573 - Spring 2018
Homework 2
This Code is to asnwer the Question 3 of homework #2
It generates an array of values and then runs a sorting 
algorithm on them
"""
import os

class glVar():
    arr = []
    directory = myFile = ''
    numComp = 0
    sortedArr = []


#The code below opens and dialog box and allows the user to select a 
#directory 
def getFilePath():
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()
    glVar.dataFiles = filedialog.askopenfilenames(parent=root,title='Select files to be tested')
    glVar.directory = os.path.dirname(glVar.dataFiles[0])
    
    file = 'TestResults_Q3_MySort.txt'
    glVar.myFile = open(os.path.join(glVar.directory, file), "a+" ) 



#Generates Array of duplicating numbers as designated by
#Homework instructions
def genArray():
    a = [1]*1024
    b = [11]*2048
    c = [111]*4096
    d = [1111]*1024
    
    glVar.arr= a+b+c+d
    print (glVar.arr)
    print (len(glVar.arr))

#sorts array considering duplicats
def holdSortDup(arr):
    it = iDup =  0
    i = 1
    while i < len(arr):
        j = i-1
               
        #Finds proper insertion point for current element item under test
        while j > 0 and arr[i] < arr[j]:
            j -= 1
            glVar.numComp += 1  

        if j != i-1:
            #Determines if there are adjacent duplicates
            iDup = findDup(i, arr, 'f')
            #jDup = findDup(j, arr, 'r')
            
            #Stores subarray of duplicates into another array
            a = arr[i:i+iDup+1]
            #print(a)
            #Removes subarray  from current position
            del arr[i:i+iDup+1]
            #Inserts subarray at proper index
            arr[j+1:j+1] = a
        else:
            glVar.numComp += 1                 
        #print (arr)
        i = i + iDup+1
        it += 1
        glVar.arr = arr
    print(it)

#The function below is used to find adjacent duplicates in an array
def findDup(index, arr, searchType):
    numDup = 0
    if searchType == "f":   
        #finds adjacent duplicates of in front of current index
        while index < len(arr)-1 and arr[index] == arr[index+1]:
            numDup += 1
            index += 1

    if searchType == "r":   
        #finds adjacent duplicates of behind current index
        while index > 0 and arr[index] == arr[index-1]:
            numDup += 1
            index -= 1
    print(numDup)
    return numDup

getFilePath()
genArray()
glVar.myFile.write('\n') 
glVar.myFile.write('Original File Arr: \n')
glVar.myFile.write(str(glVar.arr))
glVar.myFile.write('\n') 

print(glVar.arr)
holdSortDup(glVar.arr)
print(glVar.arr)
glVar.myFile.write('\n') 
glVar.myFile.write('Number of Comparisons: ')
glVar.myFile.write(str(glVar.numComp))
glVar.myFile.write('\n') 
glVar.myFile.write('Sorted File Arr: \n')
glVar.myFile.write(str(glVar.arr))

input("Press enter to exit")
