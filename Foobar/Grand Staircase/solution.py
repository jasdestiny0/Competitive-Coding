def solution(n):
    stairArray = [[0 for i in range(n + 1)] for j in range(n + 1)]
    stairArray[0][0] = 1  
    for bottom in range(1, n + 1):
        for right in range(0, n + 1):
            stairArray[bottom][right] = stairArray[bottom - 1][right]
            if right >= bottom:
                stairArray[bottom][right] += stairArray[bottom - 1][right - bottom]
    return stairArray[n][n]-1
