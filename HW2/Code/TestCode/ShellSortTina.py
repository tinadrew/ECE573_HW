"""
Tina Drew - 035006375
ECE573 - Spring 2018
Homework #2
This Code is to asnwer the Question 1 
The code runs shell short with increment values of 7, 3, and 1  and 
outputs the number of comparisons. 
"""


# Python program for implementation of Shell Sort
 
def shellSort(arr):
 
    # Start with a big gap, then reduce the gap
    N = len(arr)
    
    #Sets parameters for H or increments sequence
    hArr = [7, 3, 1]
    
    shellComp = 0
    insertComp = 0
    
    #runs elements for length of hArr   
    for h in hArr:    
        #Compares elements to the end of the array
        for i in range(0, N-h):
            j = i+h
            #numSwaps = 0
            k = j
            while k >= h:
                #swaps elements recursively until we reach the end of the array    
                if arr[i] > arr[j]: 
                    #Swap the elements if the 
                    arr[i], arr[j] = arr[j], arr[i]
                    #print (arr)
                k -= h
                j = i
                i = k                   
                                    
                #increments number of shellsort comparisions or insertions sort comparision
                if h  == 1: 
                    insertComp += 1
                else:
                    shellComp += 1
                    
    print("\nNumber of comparision for shell sort comparisons: ",shellComp)    
    print("Number of comparision for insertion sort comparisons: ", insertComp)
 
 

# Driver code to test above
arr = [10, 3, 5, 1, 7, 3, 6, 2, 8]

print ("Array before sorting:")
print(arr) 

shellSort(arr)
 
print ("\nArray after sorting:")
print(arr)
 
# This code is contributed by Mohit Kumra