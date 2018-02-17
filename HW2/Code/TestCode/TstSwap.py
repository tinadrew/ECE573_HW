
arr = [1, 3, 4, 6, 2, 2, 2, 5, 1,1, 1, 3,3, 3,2, 2,2]

def findDup():
    N = len(arr)

    # Traverse through 1 to len(arr)
    for i in range(1, N):
        x, y, xRep,yRep = 0
        y = arr[i]

        #finds adjacent duplicates of first integer
        while x == 0 and i < N:
            if arr[i] ==  arr[i+1]:
                xDup += 1
            else:
                x = arr[i]

        j = i + xDup + 1

        #finds aDJACENT duplicates of second integer        
        while y == 0 and j < N:
            if arr[j] ==  arr[y+1]:
                yDup += 1
            else:
                y = arr[j]
                print(x)
		#print(y)
    pointer = 0

N = len(arr)
print(N)

def mySort(a):
    for j in range (0, N):
        i = j-1

        x = a[i]
        y = a[j]
        
        if x > y:
            j -= 1
            
        
        pointer = 0


h = 1

def insertionSort():

    for i in range(1, N):
        #print arr[i]
        print (i)
        
        k = i
        j = i-1
        
        
        while j > 0 and arr[k] < arr[j]:
            arr[k], arr[j] = arr[j], arr[k]
            j -= 1
            k -= 1
            #print(arr[k], arr[j])
            #print(k, j)

        print (arr)


"""
This is my own version of a sorting algorithm. It is similar to insertion sort
However, holds on to the value of the current index and inserts it in proper
spot. it does not continuously swap elements on each pass.
"""
def holdSort():
    for i in range(1, N):
        j = i-1
        val =  arr[i]
        
        #Finds proper insertion point for current element item under test
        while j > 0 and val < arr[j]:
            j -= 1

        if j != i-1:
            #delete a[i] and insert into at position k
            arr.insert(j+1, arr.pop(i))
        print (arr)


def holdSortDup():
    for i in range(1, N):
        j = i-1
               
        #Finds proper insertion point for current element item under test
        while j > 0 and arr[i] < arr[j]:
            j -= 1

        if j != i-1:
            #Determines if there are adjacent duplicates
            iDup = findDup(i, arr, 'f')
            jdup = findDup(j, arr, 'r')
            
            #delete a[i] and insert into at position k
            arr.insert(j+1-jdup, arr.pop(i))
        print (arr)



def findDup(index, arr, searchType):
    numDup = 0
    if searchType == "f":   
        #finds adjacent duplicates of in front of current index
        while index < N-1 and arr[index] == arr[index+1]:
            numDup += 1
            index += 1

    if searchType == "r":   
        #finds adjacent duplicates of behind current index
        while index > 0 and arr[index] == arr[index-1]:
            numDup += 1
            index -= 1
    print(numDup)
    return numDup

findDup(3, arr, 'f')
print(arr)



print(arr)
holdSortDup()
#findDup()
print(arr)
input()

