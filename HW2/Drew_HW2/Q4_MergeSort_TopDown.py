"""Tina Drew - 035006375
ECE573 - Spring 2018
Homework 2
This Code is to asnwer the Question 3 of homework #2
It generates an array of values and then runs a sorting 
algorithm on them
"""
import os
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
    
    file = 'TestResults_Q4_MergeSort_TopDown.txt'
    glVar.myFile = open(os.path.join(glVar.directory, file), "a+" )

"""
This code was provided by:  
http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html
"""
def mergeSortTopDown(alist):
    #if outputArray == "Y" or outputArray == "y":
        #print("Splitting ",alist)
    if len(alist)>1:
        
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSortTopDown(lefthalf)
        mergeSortTopDown(righthalf)

        i=0
        j=0
        k=0
        
        while i < len(lefthalf) and j < len(righthalf):
            glVar.numComp += 1 
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
            
        #print(glVar.numComp)
        if outputArray == "Y" or outputArray == "y":
            print("Merging ",alist)
        
        print("Total Number of comparisons: ", glVar.numComp)

    #sets data array to summary of elements
   

    glVar.dataSorted = alist

    #print(alist)               

    return arr, glVar.numComp

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
        mergeSortTopDown(glVar.dataArr)
        glVar.dataSum.extend((glVar.currFile, glVar.numComp))
        writeDataFile()


getFilePath()
outputArray = input('Would you like to output the array to the screen?  Enter "Y" for yes and "N" for no: \n')

#print(glVar.dataArr)
runMergeSortBot()
print('After you exit the program, data can be reviewed in the data file here: ')
print(glVar.myFile)
input('Press enter to exit. \n')




