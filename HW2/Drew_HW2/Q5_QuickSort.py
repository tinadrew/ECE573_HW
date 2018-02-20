import random
import os

class glVar():
    dataFiles = ''
    currFile = ''
    dataArr = []
    dataSum = []
    dataSorted = []
    directory = ""
    numComp = 0
    myFile = ''
    
#The code below opens a dialog box and allows the user to select a 
#list of data files to be tested
def getFilePath():
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()
    glVar.dataFiles = filedialog.askopenfilenames(parent=root,title='Select files to be tested')
    glVar.directory = os.path.dirname(glVar.dataFiles[0])
    
    file = 'TestResults_Q5_QuickSort.txt'
    glVar.myFile = open(os.path.join(glVar.directory, file), "a+" )


#------------------------------------------------------------------
#Beginning of modified code
#This quicksort code was modified from the code here:
#https://gist.github.com/anirudhjayaraman/897ca0d97a249180a48b50d62c87f239 
def quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x)-1):
            if x[j+1] < pivot:
                x[j+1],x[i+1] = x[i+1], x[j+1]
                i += 1
            glVar.numComp += 1

            if outputArray == 'Y' or outputArray == 'y' :
                print(x)
            print('Number of comparisons: ', glVar.numComp)

        x[0],x[i] = x[i],x[0]
        first_part = quicksort(x[:i])
        second_part = quicksort(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part

#End of modified code
#------------------------------------------------------------------

#This function finds the median of the first, last, and middle element of the
#List and swaps it with the first element in the list
def medianOfThree(x):
    a = int(len(x)/2)
    b = len(x)-1

    if (x[a] <= x[0] and x[a] >= x[b]) or (x[a] >= x[0] and x[a] <= x[b]):
        x[a], x[0]  = x[0], x[a]
    elif (x[b] <= x[0] and x[b] >= x[a]) or (x[b] >= x[0] and x[b] <= x[a]):
        x[b], x[0]  = x[0], x[b]
    else:
        x = x
    return x

#b = [1, 2, 3, 4, 9, 6, 7, 5]
#alist = [54,26,93,17,77,31,44,55,20]
#print(alist)

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
    

def runQuicksortMed():  
    for f in glVar.dataFiles:
        glVar.dataSum = []
        glVar.currFile = os.path.basename(f)
        with open(f) as fi:
            data1 = fi.read().splitlines()
            glVar.dataArr = [int(x) for x in data1]
                #print(data)
        #sets valu
        glVar.numComp = 0
        #Shuffles array
        random.shuffle(glVar.dataArr)
        
        glVar.dataArr = medianOfThree(glVar.dataArr)
        dataSorted = quicksort(glVar.dataArr)
        glVar.dataSum.extend((glVar.currFile, glVar.numComp))
        writeDataFile()


getFilePath()
outputArray = input('Would you like to output the array to the screen?  Enter "Y" for yes and "N" for no: \n')

#print(glVar.dataArr)
runQuicksortMed()

print('After you exit the program, data can be reviewed in the data file here: ')
print(glVar.myFile)
input('Press enter to exit. \n')



