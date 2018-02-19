
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def insertionSort(arr):
    numComp = 0
    for i in range(0, len(arr)-1):
        k = i
        while k >= 0: 
            numComp += 1
            if arr[k] > arr[k+1]: 
                #swaps elements recursively until we reach the end of the array    
                arr[k], arr[k+1] = arr[k+1], arr[k]
                print (arr)
            else: 
                break
            k -= 1
            #increments numComp variable each time and element is swaped
    return arr, numComp               

x, y = insertionSort(arr)
print(x)
print(y)
