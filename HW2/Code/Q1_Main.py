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
    glVar.shellCompPh = 0
    glVar.insCompPh = 0
        
    N = len(arr)
    #Sets parameters for H or increments sequence
    hArr = [7, 3, 1]
    #runs elements for length of hArr   
    for h in hArr:    
        #Compares elements to the end of the array
        for i in range(0, N-h):
            j = i+h
            #numSwaps = 0
            k = j
            while k >= h and arr[i] > arr[j]: 
                #swaps elements recursively until we reach the end of the array    
                arr[i], arr[j] = arr[j], arr[i]
                #print (arr)
                k -= h
                j = i
                i = k                   
                                    
                #increments number of shellsort comparisions or insertions sort comparision
                if h  == 1: 
                    glVar.insCompPh += 1
                else:
                    glVar.shellCompPh += 1
            glVar.shellCompTot = glVar.shellCompPh + glVar.insCompPh
            print(glVar.shellCompTot)
                    
    print("\nNumber of comparision for shell sort comparisons: ", glVar.shellCompPh)    
    print("Number of comparision for insertion sort comparisons: ", glVar.insCompPh)
    #sets data array to summary of elements
    glVar.dataSum.extend((glVar.currFile, glVar.shellCompTot, glVar.shellCompPh, glVar.insCompPh))
   
    glVar.myFile.write(str(glVar.dataSum))
    glVar.myFile.write('\n')
    print('yes')

# Driver code to test above
arr = [10, 3, 5, 1, 7, 3, 6, 2, 8]

getFilePath()
#write header information to file
header = ['Datafile', 'TotShellComp', 'ShellPhaseComp', 'InsPhaseComp']
glVar.myFile.write('\n') 
glVar.myFile.write(str(header))
glVar.myFile.write('\n') 
        

def runShellSort():

    
    for f in glVar.dataFiles:
        glVar.dataSum = []
        glVar.currFile = os.path.basename(f)
        with open(f) as fi:
            glVar.dataArr = fi.read().splitlines()
            #data = [int(x) for x in data1]
                #print(data)
        shellSort(glVar.dataArr)
    #glVar.myFile.write(str(arr))
    #glVar.myFile.write(str(glVar.insCompPh))

print(glVar.dataArr)
runShellSort()
print(glVar.myFile)
input()

    
    

