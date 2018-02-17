# Hello World program in Python
class glVar():
    numDup = 0
    
    
print ("Hello World!\n")
arr = [1, 2, 4, 4, 5, 10, 100, 3, 2, 2, 2, 6, 6, 1, 10, 10, 10, 10, 4, 89]
N = len(arr)

def findDup(index, arr, searchType):

    if searchType == "f":   
        #finds adjacent duplicates of in front of current index
        while arr[index] == arr[index+1] and index < N-1:
            glVar.numDup += 1
            index += 1

    if searchType == "r":   
        #finds adjacent duplicates of behind current index
        while arr[index] == arr[index-1] and index > 0:
            glVar.numDup += 1
            index -= 1

    print(glVar.numDup)

findDup(3, arr, 'f')
print(arr)

    
""" For inserting multiple elements in an array    
print "Hello World!\n"
arr = [1, 2, 4, 4, 5, 10, 100, 3, 2, 6, 6, 1, 10, 4, 89]
list2= [2000, 3, 2]
N = len(arr)

arr = arr[:5] + list2 + arr[5:]

print(arr)
"""


