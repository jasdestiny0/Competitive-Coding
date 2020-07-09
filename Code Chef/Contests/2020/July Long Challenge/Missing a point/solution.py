# cook your dish here
testcases=int(input())
#print(testcases)
for testcase in range(testcases):
    points=int(input())
    #print(points)
    points=(4*points)-1
    x={}
    y={}
    for point in range(points):
        px,py=[int(z) for z in input().split()]
        #print(px,py)
        try:
            if x[px]==True:
                x[px]=False
        except:
            x[px]=True
        try:
            if y[py]==True:
                y[py]=False
        except:
            y[py]=True
            
    solx,soly=0,0
    #print(x,y)
    for i,j in x.items():
        if j==True:
            solx=i
            break
    for i,j in y.items():
        if j==True:
            soly=i
            break
    print(solx,soly)
    
        
