# cook your dish here

def fm(a,b,n):
    solution=None
    for c,d in a.items():
        if a[c]-b[c]==n:
            solution=c
    return solution

testcases=int(input())
for testcase in range(testcases):
    n=int(input())
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    adict={}
    bdict={}
    
    for i in a:
        if i in adict:
            adict[i]+=1
        else:
            adict[i]=1
            bdict[i]=0
    for i in b:
        if i in bdict:
            bdict[i]+=1
        else:
            bdict[i]=1
        
        if i not in adict:
            adict[i]=0

    flag=True
    cost=0
    #print(adict,bdict)
    for k,v in adict.items():
        if adict[k]==bdict[k]:
            continue
        elif adict[k]<bdict[k]:
            if (bdict[k]-adict[k])%2!=0:
                print(-1)
                flag=False
                break
            findMatch=fm(adict,bdict,bdict[k]-adict[k])
            if findMatch==None:
                flag=False
                print(-1)
                break
            else:
                cost+=(((bdict[k]-adict[k])/2) *k)
                adict[k]=bdict[k]=(adict[k]+bdict[k])/2
                adict[findMatch]=bdict[findMatch]=((adict[findMatch]+bdict[findMatch])/2)

        else:
            if (adict[k]-bdict[k])%2!=0:
                print(-1)
                flag=False
                break
            findMatch=fm(bdict, adict, adict[k]-bdict[k])
            if findMatch==None:
                flag=False
                print(-1)
                break
            else:
                cost+=(((adict[k]-bdict[k])/2) *k)
                adict[k]=bdict[k]=(adict[k]+bdict[k])/2
                adict[findMatch]=bdict[findMatch]=((adict[findMatch]+bdict[findMatch])/2)
    if flag:
        print(cost)

