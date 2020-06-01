def findThreeLargestNumbers(array):
    firstLargest=float("-inf")
    secondLargest=float("-inf")
    thirdLargest=float("-inf")
    for i in array:
        if i>firstLargest:
            thirdLargest=secondLargest
            secondLargest=firstLargest
            firstLargest=i
        elif i>secondLargest:
            thirdLargest=secondLargest
            secondLargest=i
        elif i>thirdLargest:
            thirdLargest=i
    return [thirdLargest,secondLargest,firstLargest]
