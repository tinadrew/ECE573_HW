


#This function finds the median of the first, last, and middle element of the
#List and swaps it with the first element in the list
def kendallTauDistance(a1, a2):

    distance = 0
    numComp = 0
    for i in range (0, len(a1)):
        numComp += 1
        for j in range (i, len(a1)):
            numComp += 1
            
            if (a1[i]- a1[j])*(a2[i]- a2[j]) > 0: 
                distance += 1
            else:
                break
            
            j += 1
            #
    print(numComp)
    return distance



a1 = [1, 2, 3, 4, 5]
a2 = [5, 4, 3, 2, 1]


print(kendallTauDistance(a1, a2))
