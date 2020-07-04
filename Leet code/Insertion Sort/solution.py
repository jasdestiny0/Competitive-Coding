def insertionSort(array):
    lengthOfArray=len(array)
    for i in range(1,lengthOfArray,1):
        if array[i-1]>array[i]:
            j=i
            while array[j-1]>array[j] and j>0:
                array[j],array[j-1]=array[j-1],array[j]
                j-=1
    return array
