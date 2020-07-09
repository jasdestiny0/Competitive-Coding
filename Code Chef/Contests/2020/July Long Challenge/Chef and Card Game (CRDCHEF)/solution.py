# cook your dish here
testcases=int(input())
for testcase in range(testcases):
    rounds=int(input())
    c=0
    m=0
    for round in range(rounds):
        x=[[int(x) for x in str(y)] for y in input().split()]
        cp=sum(x[0])
        mp=sum(x[1])
        if cp>mp:
            c+=1
        elif mp>cp:
            m+=1
    if c>m:
        print(0,c)
    elif m>c:
        print(1,m)
    else:
        print(2,c)
