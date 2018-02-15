"""Tina Drew - 035006375
ECE573 - Spring 2018
Homework 1
This Code is to answer Question 4  of homework #1
"""

#Imports Library to use timing function
import time

#Sets global variables to default variables
startProg = time.time()
timeFarthest = 0
timeProg = 0
SumCount = 0
OpCount = 0
N = 0
arrN = []
arrNaive = []
pair = []
    
#arr = [-10, 10, 1, 0, 20, 10, 25, 5, 30]
#arrN = [] #X axis for inputs
#arrNaive = []
#arrNaive = []
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

def FarthestSum(data):
    global SumCount
    SumCount = 0
    global OpCount
    OpCount = 0 
    global timeProg
    global pair
    global diff
    N = len(data)
    data.sort()
    pair = [data[0], data[N-1]]
    diff = data[N-1] - data[0]
       
    return SumCount, OpCount, timeFarthest
    
def runFarthest():
#Gets data from each file with a .txt extension in the directory
#Part of the code is referenced from 
#http://www.pitt.edu/~naraehan/python2/file_path_cwd.html
    import os
    global data
    global arrN
    global arrNaive
    global arrBinSum
    global N
    global timeFarthest
    
    path = os.path.dirname(getFilePath())
    print(path)
    
    for file in os.listdir(path):
        fNew =  os.path.join(path, file)
            #https://stackoverflow.com/questions/3277503/how-do-i-read-a-file-line-by-line-into-a-list
        if fNew.endswith(".txt"):
            #print(fNew)
            startFarthest = time.time()
            with open(fNew) as f:
                data1 = f.read().splitlines()
                data = [float(x) for x in data1]
                N = len(data)
                #print(data)
            FarthestSum(data)
            timeFarthest = time.time() - startFarthest
            arrN.append(N)
            arrNaive.append(round(1000*timeFarthest, 2))
            
            
            print("\n")
            print("N: ", N)
            print("Time: ", timeFarthest)
            print("Pair = ", pair)
            print("Diff = ", diff)
        
runFarthest()
#print("\n", "Input values of unsorted N: ", arrN) 

arrFarthestS = [arrNaive for _,arrNaive in sorted(zip(arrN,arrNaive))]
#arrBinSumS = [arrBinSum for _,arrBinSum in sorted(zip(arrN,arrBinSum))]
arrN.sort()

print("\n")
print("Number of inputs (N): ", arrN) 
print ("Time for algorithm (ms): ", arrFarthestS)
#print(arrNaive)


#print ("Time of Bin Search Implementation", arrBinSumS)


#import matplotlib.pyplot as plt
#X = [590,540,740,130,810,300,320,230,470,620,770,250]
#Y = [32,36,39,52,61,72,77,75,68,57,48,48]
#plt.scatter(X,Y)

input ()
