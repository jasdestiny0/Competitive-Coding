def solution(strList):
    dict1={x[1:]:True for x in strList}
    return len(dict1)

print(solution([""]))
