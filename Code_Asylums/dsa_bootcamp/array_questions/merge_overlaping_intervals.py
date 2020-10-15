def overlap_interval(arr):
    if not arr:
        return []
    arr=sorted(arr, key=lambda x:x[0])
    soln=[arr[0]]
    for i in range(1, len(arr), 1):
        if arr[i][0]<soln[-1][1]:
            soln[-1][1]=arr[i][1]
        else:
            soln.append(arr[i])
    return soln
print(overlap_interval([[1,3],[2,4],[5,7],[6,8]]))