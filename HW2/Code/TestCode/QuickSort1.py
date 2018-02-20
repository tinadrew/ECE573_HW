import random

#------------------------------------------------------------------
#Beginning of modified code
#This quicksort code was modified from the code here:
#https://gist.github.com/anirudhjayaraman/897ca0d97a249180a48b50d62c87f239 
def quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x)-1):
            if x[j+1] < pivot:
                x[j+1],x[i+1] = x[i+1], x[j+1]
                i += 1
            print(x)
        x[0],x[i] = x[i],x[0]
        first_part = quicksort(x[:i])
        second_part = quicksort(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part

#End of modified code
#------------------------------------------------------------------

#This function finds the median of the first, last, and middle element of the
#List and swaps it with the first element in the list
def medianOfThree(x):
    a = int(len(x)/2)
    b = len(x)-1

    if (x[a] <= x[0] and x[a] >= x[b]) or (x[a] >= x[0] and x[a] <= x[b]):
        x[a], x[0]  = x[0], x[a]
    elif (x[b] <= x[0] and x[b] >= x[a]) or (x[b] >= x[0] and x[b] <= x[a]):
        x[b], x[0]  = x[0], x[b]
    else:
        x = x
    return x
b = [1, 2, 3, 4, 9, 6, 7, 5]
alist = [54,26,93,17,77,31,44,55,20]
print(alist)

#Shuffles array
random.shuffle(alist)

print(alist)
#print(quicksort(alist))

print(medianOfThree(b))


