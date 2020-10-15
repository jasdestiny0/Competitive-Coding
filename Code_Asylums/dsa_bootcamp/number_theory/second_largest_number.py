def second_largest_number(arr):
    soln=[None,None]
    maxElem=float("-inf")
    for i in arr:
        if i>maxElem:
            soln[1], soln[0]= soln[0], i
    return soln[1]
print(second_largest_number([2, 35, 1, 10, 34, 1]))