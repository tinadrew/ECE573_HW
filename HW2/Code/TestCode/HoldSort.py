def holdSort(arr):
    for i in range(1, len(arr)):
        j = i-1
        comp = 0
        #updates the number of comparison each time the loop runs
        #Finds proper insertion point for current element item under test
        while j >= 0 and arr[i] < arr[j]: 
            comp += 1
            j -= 1 
        if j != i-1:
            glVar.numComp += comp
            #delete a[i] and insert into at position k
            arr.insert(j+1, arr.pop(i))
        else:
            glVar.numComp +=1
        #print (comp)
    print(glVar.numComp)
    return arr, glVar.numComp
