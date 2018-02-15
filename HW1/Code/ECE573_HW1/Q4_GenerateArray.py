"""Tina Drew - 035006375
ECE573 - Spring 2018
Homework 1
This Code is to provide a data set for  the Question 4  of homework #1
It create a set random floating point numbers and prints the to file. 
The size of the list or array is based on the user input value of N.  
"""


import random

def getFilePath():
    import tkinter as tk
    from tkinter import filedialog
    global fileNew
    root = tk.Tk()
    root.withdraw()
    fileNew = filedialog.askopenfilename()
    return fileNew

getFilePath()
afile = open(fileNew, "w" )

#Writes random vairables for file.  Based on code from:
#https://stackoverflow.com/questions/14907759/random-number-file-writer
for i in range(int(input('How many random numbers?: '))):
    a = random.uniform(-100, 100)
    line = '%.2f' %a +'\n'
    afile.write(line)
    print(line)

afile.close()
#print('all done')