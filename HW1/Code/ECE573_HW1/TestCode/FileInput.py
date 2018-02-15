#used to open a dialog box and select the path
import tkinter as tk
from tkinter import filedialog
global data
global N
root = tk.Tk()
root.withdraw()
fileName = filedialog.askopenfilename()

#Gets data from each file with a .txt extension in the directory
#http://www.pitt.edu/~naraehan/python2/file_path_cwd.html
import os
path = os.path.dirname(fileName)
print(path)

for file in os.listdir(path):
    fNew =  os.path.join(path, file)
        #https://stackoverflow.com/questions/3277503/how-do-i-read-a-file-line-by-line-into-a-list
    if fNew.endswith(".txt"):
        #print(fNew)
        with open(fNew) as f:
            data1 = f.read().splitlines()
            data = [int(x) for x in data1]
            N = len(data)
            print(data)
            
        