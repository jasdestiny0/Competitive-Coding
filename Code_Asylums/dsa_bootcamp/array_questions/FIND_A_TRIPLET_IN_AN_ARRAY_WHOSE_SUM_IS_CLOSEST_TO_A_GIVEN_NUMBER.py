def triple_sum(arr, num):
    if len(arr)<3:
        return None
    arr.sort()
    smallestDiff=float("inf")
    sumSoln=float("inf")
    for i in range(0,len(arr)-1,1):
        p1=i+1
        p2=len(arr)-1
        while p1<p2:
            currentSum=arr[i]+arr[p1]+arr[p2]
            if abs(num-currentSum)<smallestDiff:
                smallestDiff=num-currentSum
                sumSoln=currentSum
            if num<currentSum:
                p1+=1
            elif num>currentSum:
                p2-=1
            else:
                break
    return sumSoln
print(triple_sum([-1, 1, 1, -4], 1))
