def powerset(array):
    solution=[]
    checklist=[[0 for i in array] for j in range(2**(len(array)))]
    for i in range(1,len(checklist),1):
        checklist[i]=checklist[i-1].copy()
        current=[]
        for k in range(0,len(checklist[0]),1):
            if checklist[i][k]*array[k]!=0:
                current.append(checklist[i][k]*array[k])
        solution.append(current)
        print(checklist[i])
        for j in range(0,len(checklist[0]),1):
            if checklist[i][j]==0:
                checklist[i][j]=1
                break
            else:
                checklist[i][j]=0
    solution.append(array)
    return solution
    
