import math
def sum_less_than_x(arr, x):
    n=1
    for i in range(0, len(arr)-1):
        if arr[i]+arr[i+1]> x:
            break
        n+=1
    return int(math.factorial(n)/((math.factorial(n-2))*2)) if n>1 else 0
print(sum_less_than_x([1,2,3,4,5,6],7))