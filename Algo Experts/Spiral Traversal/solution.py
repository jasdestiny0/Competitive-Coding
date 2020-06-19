def spiralTraverse(array):
    solution=[]
    xlen=len(array[0])
    ylen=len(array)
    x=-1
    y=0
    total=xlen*ylen
    count=0
    while xlen>0 and ylen>0:
        for xiter in range(xlen):
            x+=1
            solution.append(array[y][x]) 
            count+=1
        xlen-=1
        
        if count==total:
                break
            
        ylen-=1
        for yiter in range(ylen):
            y+=1
            solution.append(array[y][x])
            count+=1
        
        for xiter in range(xlen):
            x-=1
            solution.append(array[y][x])
            count+=1
        xlen-=1
        
        if count==total:
                break
        
        ylen-=1
        for yiter in range(ylen):
            y-=1
            solution.append(array[y][x])
            count+=1
    
    
    
    return solution

print(spiralTraverse([[1, 2, 3, 4], 
                      [10, 11, 12, 5], 
                      [9, 8, 7, 6]]))
