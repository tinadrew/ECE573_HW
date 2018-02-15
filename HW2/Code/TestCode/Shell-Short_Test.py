import numpy 

# Code based on code from  https://www.geeksforgeeks.org/shellsort/
# Python program for implementation of Shell Sort
 
def shellSort(arr):
 
    # Start with a big gap, then reduce the gap
    n = len(arr)
    shellComp = 0;
    insComp = 0
    #gap = n/2

    #gap = 3
    gapArr = [3, 1]
    hInd = 0
    gap = gapArr[hInd]
   
    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped 
    # order keep adding one more element until the entire array
    # is gap sorted
    
    for x in range(0, len(gapArr)):
        gap = gapArr[hInd]
        for i in range(gap,n):
            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = arr[i]
 
            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            while  j >= gap: 
                if gap == 1:
                    insComp += 1
                else: 
                    shellComp += 1
                if arr[j-gap] >temp:
                    arr[j] = arr[j-gap]
                j -= gap
 
            # put temp (the original a[i]) in its correct location
            
            arr[j] = temp
            print(arr)
        hInd -= 1    
    return insComp, shellComp
 
 
# Driver code to test above
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


print ("Array before sorting:")
print(arr)

n = len(arr)
shellSort(arr)


print ("\nArray after sorting:")
print(arr)


#print(insComp)
#print(shellComp)
 
# This code is contributed by Mohit Kumra