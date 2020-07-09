# cook your dish here
testcases=int(input())
for testcase in range(testcases):
    n=int(input())
    arr=[int(x) for x in input().split()]
    number=0
    for i in range(0,n-1,1):
        if arr[i]!=arr[i+1]:
            number+=abs(arr[i]-arr[i+1])-1
    print(number)
