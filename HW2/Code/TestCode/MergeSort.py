

class glVar: 
    numComp = 0

"""
This code was provided by:  
http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html
"""
def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        
        while i < len(lefthalf) and j < len(righthalf):
            glVar.numComp += 1 
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
            
    print(glVar.numComp)
    print("Merging ",alist)

alist = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
mergeSort(alist)
print(alist)

