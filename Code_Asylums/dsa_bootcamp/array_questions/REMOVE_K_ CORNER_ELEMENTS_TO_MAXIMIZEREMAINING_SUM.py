def k_corner(arr, k):
    if len(arr)<k:
        return 0
    maxSum=float("-inf")
    currentSum=sum(arr[0:len(arr)-k])
    ws=len(arr)-k
    for i in range(1,len(arr)-ws):
        currentSum-=arr[i-1]
        currentSum+=arr[i+ws-1]
        maxSum=max(maxSum, currentSum)
    return maxSum
print(k_corner([11, 49, 100, 20, 86, 29, 72],4))