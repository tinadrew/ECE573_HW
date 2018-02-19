"""
Tina Drew - 035006375
ECE573 - Spring 2018
Homework #2
This Code is to asnwer the Question 1 
The code runs shell short with increment values of 7, 3, and 1  and 
outputs the number of comparisons. 
"""
import os

class glVar():
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
    
#The code below opens and dialog box and allows the user to select a 
#directory 
def getFilePath():
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()
    glVar.dataFiles = filedialog.askopenfilenames(parent=root,title='Select files to be tested')
    glVar.directory = os.path.dirname(glVar.dataFiles[0])
    
    file = 'TestResults.txt'
    glVar.myFile = open(os.path.join(glVar.directory, file), "a+" )
    
# Python program for implementation of Shell Sort
#Based loosely on code from https://www.geeksforgeeks.org/shellsort/
def shellSort(arr):
    # Start with a big gap, then reduce the gap
    glVar.shellCompPh = glVar.insCompPh = 0
            
    N = len(arr)
    #Sets parameters for H or increments sequence
    hArr = [7, 3, 1]
    #runs elements for length of hArr   
    for h in hArr:    
        #Compares elements to the end of the array
        for i in range(0, N-h):
            #numSwaps = 0
            while i >= 0: 
                #increments number of shellsort comparisions or insertions sort comparision
                if h  == 1: 
                    glVar.insCompPh += 1
                else:
                    glVar.shellCompPh += 1
                if arr[i] > arr[i+h]: 
                    #swaps elements recursively until we reach the end of the array    
                    arr[i], arr[i+h] = arr[i+h], arr[i]
                    #print (arr)
                    i -= h
                else:
                    break   
            glVar.shellCompTot = glVar.shellCompPh + glVar.insCompPh
            print(glVar.shellCompTot)
            glVar.dataSorted = arr
    
    #arr, glVar.insCompPh =  insertionSort(arr)           
            
    glVar.shellCompTot = glVar.shellCompPh + glVar.insCompPh
    print(glVar.shellCompTot)
            
    print(arr)               
    print("\nNumber of comparision for shell sort comparisons: ", glVar.shellCompPh)    
    print("Number of comparision for insertion sort comparisons: ", glVar.insCompPh)
    #sets data array to summary of elements
    glVar.dataSum.extend((glVar.currFile, glVar.shellCompTot, glVar.shellCompPh, glVar.insCompPh))


    print(glVar.dataSum)


def writeDataFile():
    #write header information to file
    header = ['Datafile', 'TotShellComp', 'ShellPhaseComp', 'InsPhaseComp']
    glVar.myFile.write('\n') 
    glVar.myFile.write(str(header))
    glVar.myFile.write('\n')           
    glVar.myFile.write(str(glVar.dataSum))
    glVar.myFile.write('\nSorted array: \n')
    glVar.myFile.write(str(glVar.dataSorted))
    glVar.myFile.write('\n')
    

def runShellSort():  
    for f in glVar.dataFiles:
        glVar.dataSum = []
        glVar.currFile = os.path.basename(f)
        with open(f) as fi:
            data1 = fi.read().splitlines()
            glVar.dataArr = [int(x) for x in data1]
                #print(data)
        print(glVar.dataArr)
        shellSort(glVar.dataArr)
        writeDataFile()


# Driver arrays code to test above
a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = [10, 5, 9, 6, 13, 3, 1, 2, 18]

getFilePath()
print(glVar.dataArr)
runShellSort()
print('After you exit the program, data can be reviewed in the data file here: ')
print(glVar.myFile)
input('Press enter to exit. \n')

    
    

