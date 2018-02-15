"""Tina Drew - 035006375
ECE573 - Spring 2018
Homework 1
This Code is to asnwer the Question 2 of homework #1
It runs the Quick Find algorithm and outputs the results.
"""


import time

filePath2 = ""
files = []
arr = []
data = []
pList = []
qList = []
idList= []
algorTime = []
arrN = []
N = 0

def genIndList():
    global idList
    for i in range(0, 8191):
        idList.append(i)
    return idList 
        

#Used to open the file dialog box.  Copied from:
#https://stackoverflow.com/questions/9319317/quick-and-easy-file-dialog-in-python/14119223
def getFileList():
    import tkinter as tk
    import os
    global files
    global filepath2
    from tkinter import filedialog
    files = []
    root = tk.Tk()
    root.withdraw()
    
    filePath = filedialog.askopenfilename()
    #filePath2 = filedialog.askopenfilename()
    
    path = os.path.dirname(filePath)
    #print(path)
    
    for file in os.listdir(path):
        fNew =  os.path.join(path, file)
            #https://stackoverflow.com/questions/3277503/how-do-i-read-a-file-line-by-line-into-a-list
        if fNew.endswith(".txt"):
            files.append(fNew)    
            #print(fNew)
    return files

def getDataList(datafile):
    global pList
    global qList
    global N
    
    with open(datafile) as f:
        data1 = f.read().splitlines()
        #h = data1.split(" ")
        N = len(data1)
        arrN.append(N)
        for i in range(0, N-1):
            data.append(data1[i].split())
            
        #This section of the code is used the break up the data in the P and Q list
        #Part of the code is derived from
        #https://snakify.org/lessons/two_dimensional_lists_arrays/
        for row in data:
            i = 0
            for elem in row: 
                if i > 0:
                    qList.append(int(elem))
                else: 
                    pList.append(int(elem))
                i = 1
        #print("P List: ", pList)
        #print("Q List: ", qList, "\n")
        return
    

def quickFind():
    
    #print('all done')
    
    startAlgor = time.time()
    #global idList
    print("\nUnion pairs for N = ", N,"\n")
    print(idList)
    global pairs
    pairs = []
    pid = 0 
    qid = 0
    #afile = open(filePath2, "w" )
    #afile.write("\nUnion pairs \n")
 
    for i in range(0, N-1):
        p = pList[i]
        q = qList[i]
        
        if p != q:
            pid = idList[p] 
            qid = idList[q]
            print(pid, ", ", qid)
            #pairs.append(pid, qid)
            union (pid, qid)                
    
    #afile.close()
    #appends current time to the array
    algorTime.append(round((time.time() -startAlgor), 2))

def union (pid, qid):
    #print("\n Union pairs: ")
    global idList
    for x in range(0, len(idList)):
        if idList[x] == pid:
            idList[x] = qid

def runQuickFind():
    getFileList()
    
    for x in range(0, len(files)):
        genIndList()
        getDataList(files[x])
        quickFind()
        #print(idList)

runQuickFind()

algorTime = [algorTime for _,algorTime in sorted(zip(arrN,algorTime))]
arrN.sort()


print("\nInput size (N): ", arrN)
print("Algorithm time:", algorTime)


input("\n ALL DONE! Press any key to exit. ")
