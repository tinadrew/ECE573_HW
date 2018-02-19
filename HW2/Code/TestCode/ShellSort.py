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


#getFilePath()
#write header information to file
header = ['Datafile', 'TotShellComp', 'ShellPhaseComp', 'InsPhaseComp']
#glVar.myFile.write('\n') 
#glVar.myFile.write(str(header))
#glVar.myFile.write('\n')
#Code from https://www.geeks
    glVar.shellCompPh = 0
    glVar.insCompPh = 0

    N = len(arr)
    
    # Traverse through 1 to len(arr)
    for i in range(1, N):
        x, y, xRep,yRep = 0
        y = arr[i]

        #finds adjacent duplicates of first integar
        while x == 0 and i < N:
            if arr[i] ==  arr[i+1]:
                xDup += 1
            else x = arr[i]

        j = i + xDup + 1

        #finds aDJACENT duplicates of second integar        
        while y == 0 and j < N:
            if arr[j] ==  arr[y+1]:
                yDup += 1
            else y = arr[j]


        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and y < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
            glVar.insCompPh += 1
        arr[j+1] = y

        

        glVar.shellCompTot = glVar.shellCompPh + glVar.insCompPh
        print(glVar.shellCompTot)
                
    print("\nNumber of comparision for shell sort comparisons: ", glVar.shellCompPh)    
    print("Number of comparision for insertion sort comparisons: ", glVar.insCompPh)
    #sets data array to summary of elements
    glVar.dataSum.extend((glVar.currFile, glVar.shellCompTot, glVar.shellCompPh, glVar.insCompPh))
    

def runShellSort():

    arr = [10, 3, 5, 1, 7, 2, 2, 2, 3, 6, 2, 8]
    arr2 = [2,2,2,2,1,1,3,3] 
    glVar.dataSum = []
    glVar.dataArr = arr
    print(arr)

    insertionSort(glVar.dataArr)
    #glVar.myFile.write(str(arr))
    #glVar.myFile.write(str(glVar.insCompPh))


runShellSort()
print(glVar.dataArr)
input('Hit enter to exit')
