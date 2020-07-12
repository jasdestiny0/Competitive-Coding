
testcases=int(input())
#print(testcases)
for testcase in range(testcases):
    n,dailyLimit=[int(x) for x in input().split()]
    #print(n,dailyLimit)
    cases=[int(x) for x in input().split()]
    cases=sorted(cases)
    index=0
    days=0
    limit=cases.copy()
    #print("limit",limit)
    while index<n:
        cases[index]-=dailyLimit
        days+=1
        cases[index]=(2*cases[index])
        if cases[index]>limit[index]:
            cases[index]=limit[index]
        #print("day",days,cases[index],limit[index])
        dailyLimit*=2
        #print(days, index, cases[index],dailyLimit)
        if cases[index]<=0:
            index+=1
    print(days)
        
    
