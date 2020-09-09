# cook your dish here
testcases=int(input())
for testcase in range(testcases):
    n=int(input())
    dict1={}
    s=list(map(int,input().split()))
    for i in s:
        dict1[i]=True
    print(len(dict1))