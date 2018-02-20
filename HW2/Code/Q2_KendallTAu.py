
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
    distance = 0
   
#The code below opens and dialog box and allows the user to select a 
#directory 
def getFilePath():
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()
    glVar.dataFiles = filedialog.askopenfilenames(parent=root,title='Select files to be tested')
    glVar.directory = os.path.dirname(glVar.dataFiles[0])
    
    file = 'TestResults_Q2_KendalTau.txt'
    glVar.myFile = open(os.path.join(glVar.directory, file), "a+" )

#This function finds the median of the first, last, and middle element of the
#List and swaps it with the first element in the list
def kendallTauDistancNiave(a):

    glVar.distance = 0
    glVar.numComp = 0
    for i in range (0, len(a)-1):
        for j in range (i, len(a)-1):
           glVar.numComp += 1
           if a[j] > a[j+1]:
                glVar.distance += 1
    print("Number of comparision for comparisons: ", glVar.numComp)
    print("Kendal Tau Distance: ", glVar.distance)
    
    return glVar.distance
    
    #sets data array to summary of elements
    glVar.dataSum.extend((glVar.currFile, glVar.numComp, glVar.distance))
   
    return arr, glVar.numComp


def writeDataFile():
    #write header information to file
    header = ['Datafile', 'NumComp', 'Distance']
    glVar.myFile.write('\n') 
    glVar.myFile.write(str(header))
    glVar.myFile.write('\n')           
    glVar.myFile.write(str(glVar.dataSum))
    glVar.myFile.write('\nSorted array: \n')
    glVar.myFile.write(str(glVar.dataSorted))
    glVar.myFile.write('\n')
    

def runKedallTauDistance():  
    for f in glVar.dataFiles:
        glVar.dataSum = []
        glVar.currFile = os.path.basename(f)
        with open(f) as fi:
            data1 = fi.read().splitlines()
            glVar.dataArr = [int(x) for x in data1]
                #print(data)
        #print(glVar.dataArr)
        kendallTauDistancNiave(glVar.dataArr)
        writeDataFile()


getFilePath()
#outputArray = input('Would you like to output the array to the screen?  Enter "Y" for yes and "N" for no: \n')

#print(glVar.dataArr)
runKedallTauDistance()
print('After you exit the program, data can be reviewed in the data file here: ')
print(glVar.myFile)
input('Press enter to exit. \n')


a = [3, 5,7, 1, 2, 0, 13, 54, 6]


print(kendallTauDistanceQuick(a))
