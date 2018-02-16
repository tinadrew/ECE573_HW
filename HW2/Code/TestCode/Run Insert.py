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

#
# Python program for implementation of Shell Sort
#Based loosely on code from https://www.geeksforgeeks.org/shellsort/
def shellSort(arr):
    glVar.shellCompPh = 0
    glVar.insCompPh = 0
        
    N = len(arr)

    #runs elements for length of hArr   
    h = 1
    for i in range(0, N-1):
        j = i+1
        #numSwaps = 0
        k = j
        while k >= 0 and arr[i] > arr[j]: 
            #swaps elements recursively until we reach the end of the array    
            arr[i], arr[j] = arr[j], arr[i]
            #print (arr)
                
            k -= 1
            j = i
            i = k                   
                                
            #increments number of shellsort comparisions or insertions sort comparision
          
            glVar.insCompPh += 1

        glVar.shellCompTot = glVar.shellCompPh + glVar.insCompPh
        print(glVar.shellCompTot)
                
    print("\nNumber of comparision for shell sort comparisons: ", glVar.shellCompPh)    
    print("Number of comparision for insertion sort comparisons: ", glVar.insCompPh)
    #sets data array to summary of elements
    glVar.dataSum.extend((glVar.currFile, glVar.shellCompTot, glVar.shellCompPh, glVar.insCompPh))
    
    #glVar.myFile.write(str(glVar.dataSum))
    #glVar.myFile.write('\n') 

# Driver code to test above


#getFilePath()
#write header information to file
header = ['Datafile', 'TotShellComp', 'ShellPhaseComp', 'InsPhaseComp']
#glVar.myFile.write('\n') 
#glVar.myFile.write(str(header))
#glVar.myFile.write('\n') 
        

def runShellSort():

    arr = [10, 3, 5, 1, 7, 3, 6, 2, 8]
    glVar.dataSum = []
    glVar.dataArr = arr
    print(arr)

    shellSort(glVar.dataArr)
    #glVar.myFile.write(str(arr))
    #glVar.myFile.write(str(glVar.insCompPh))


runShellSort()
print(glVar.dataArr)
print("HelloWORLD")
    
    
