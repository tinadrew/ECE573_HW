"""
Tina Drew - 035006375
ECE573 - Spring 2018
Homework 1
This Code is to asnwer the Question 5 of homework #1

"""

#Imports Library to use timing function
import time

#Sets global variables to default variables
startProg = time.time()
timeSumLinSearch = 0
timeProg = 0
SumCount = 0
OpCount = 0
N = 0
arrN = []
arrLinSum = []
    
arr = [-10, 10, 1, 0, 20, 10, 25, 5, 30]
arrLog = []

#Used to open the file dialog box.  Copied from:
#https://stackoverflow.com/questions/9319317/quick-and-easy-file-dialog-in-python/14119223
def getFilePath():
    import tkinter as tk
    from tkinter import filedialog
    global filePath
    root = tk.Tk()
    root.withdraw()
    filePath = filedialog.askopenfilename()
    return filePath
    
#The function below provides a naive implementation 
#of the three sum problem.  The code is based on 
#Slide 34 for the fundamentals-1-s18 slides


def ThreeSumLinSearch(array):
    startSumLinSearch = time.time()
    global SumCount
    SumCount = 0
    global OpCount
    OpCount = 0 
    global timeSumLinSearch
    data = array
    data.sort()
    #print(data)
    N = len(data)
    for i in range(0, N-1):
        for j in range(i+1, N-1):
            item = -(data[i] + data [j])
            #print(item)
            if linearSearch(data, item): 
                SumCount = SumCount+1
                #print(data[i], data[j], item)
                
    timeSumLinSearch = time.time() - startSumLinSearch
    #print("Number of tuples: ", SumCount)
    #print("Number of operations: ", OpCount)
    return SumCount, OpCount, timeSumLinSearch


def linearSearch(alist, item): 
    found = False
  
    for j in range(0, N-1):
        if alist[j] == item:
            #print(j)
            found = True
            break
        elif alist[j] > item:
            break
        
    return found

    
#The function below prints information from the program   
def printData(data, OpCount, SumCount, timeProg, timeNaive, N):                         
    print("Length or array: ", N)
    print("Number of 3 sum pairs =", SumCount)
    print("Number of operations =", OpCount)
    print ("Program Time =", timeProg)
    print ("Algorithm Time =", timeNaive)



#ThreeSumNaive(data)
#printData(data, OpCount, SumCount, timeProg, timeNaive, N)

def runThreeSum():
#Gets data from each file with a .txt extension in the directory
#Part of the code is referenced from 
#http://www.pitt.edu/~naraehan/python2/file_path_cwd.html
    import os
    global data
    global arrN
    global arrNaive
    global arrBinSum
    global arrLinSum
    global N
    
    path = os.path.dirname(getFilePath())
    print(path)
    print("\nN", "    Alg Time", "    Pairs")
    for file in os.listdir(path):
        fNew =  os.path.join(path, file)
            #https://stackoverflow.com/questions/3277503/how-do-i-read-a-file-line-by-line-into-a-list
        if fNew.endswith(".txt"):
            #print(fNew)
            with open(fNew) as f:
                data1 = f.read().splitlines()
                data = [int(x) for x in data1]
                N = len(data)
            
            ThreeSumLinSearch(data)
            arrN.append(N)
            arrLinSum.append(round(timeSumLinSearch, 2))
            
            print(N,",    ", round(timeSumLinSearch, 2),",    ", SumCount)   
        
runThreeSum()

arrLinSumS = [arrLinSum for _,arrLinSum in sorted(zip(arrN,arrLinSum))]

arrN.sort()


print("\nInput values of N: ", arrN) 
print ("Time of Linear Search Implementation", arrLinSumS)

#import matplotlib.pyplot as plt
#X = [590,540,740,130,810,300,320,230,470,620,770,250]
#Y = [32,36,39,52,61,72,77,75,68,57,48,48]
#plt.scatter(X,Y)

input ("Press return to exit")
