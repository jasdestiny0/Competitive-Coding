testcases=int(input())
for testcase in range(testcases):
    string='O'
    n=int(input())
    solution=[]
    for i in range(2,n+1):
        string+="."
        if i%8==0:
            solution.append(string)
            string=""
    for j in range(n+1,65):
        string+='X'
        if j%8==0:
            solution.append(string)
            string=""
    
    for i in solution:
        print(i)
        
    
