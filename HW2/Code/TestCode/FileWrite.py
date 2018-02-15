#Used to open the file dialog box.  Copied from:
#https://stackoverflow.com/questions/9319317/quick-and-easy-file-dialog-in-python/14119223

import random
#The code below opens and dialog box and allows the user to select a 
#directory 
class glVar():
    filePath = ''
    directory = ""

#The code below opens and dialog box and allows the user to select a 
#directory 
def getFilePath():
    import tkinter as tk
    from tkinter import filedialog
    import os

    root = tk.Tk()
    root.withdraw()
    glVar.filePath = filedialog.askopenfilenames(parent=root,title='Select files to be tested')
    glVar.directory = os.path.dirname(glVar.filePath[0])

#The code below opens or creates a new files. 
import os
getFilePath()
file = 'test.data'
fNew =  os.path.join(glVar.directory, file)
afile = open(fNew, "w+" )
#Writes random vairables for file.  Based on code from:
#https://stackoverflow.com/questions/14907759/random-number-file-writer
for i in range(int(input('How many random numbers?: '))):
    a = random.uniform(-100, 100)
    line = '%.2f' %a +'\n'
    afile.write(line)
    print(line)

afile.close()
#print('all done')