testcases=int(input())
for testcase in range(testcases):
    n=int(input())
    l=list(map(int,input().split()))
    if n<3:
        print("Case #"+str(testcase+1)+": "+str(n))
        continue
    longest=2
    current=2
    diff=l[1]-l[0]
    for i in range(2,n,1):
        if diff==l[i]-l[i-1]:
            current+=1
        else:
            current=2
            diff=l[i]-l[i-1]
        longest=max(longest,current)
    print("Case #"+str(testcase+1)+": "+str(longest))
    
