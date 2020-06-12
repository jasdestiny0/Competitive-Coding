testcases=int(input())
for t in range(testcases):
    length,m=[int(x) for x in input().split()]
    expectedArray=[x for x in range(m,0,-1)]
    count=0
    array=[int(x) for x in input().split()]
    for i in range(0,length,1):
        if array[i]==m:
            for j in range(0,m,1):
                if array[i+j]!=expectedArray[j]:
                    i+=j-1
                    break
                if j==m-1:
                    count+=1
                    i+=j-1     
    print("Case #"+str(t+1)+": "+str(count))
            
