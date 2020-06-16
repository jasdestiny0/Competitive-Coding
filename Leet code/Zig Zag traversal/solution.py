def zigzagTraverse(array):
    lenx=len(array[0])
    leny=len(array)
    x=0
    y=0
    solution=[]
    traversalMode=True
    while x<lenx and y<leny:
        solution.append(array[y][x])
        
        if x==lenx-1 and not traversalMode:
            y+=1
            traversalMode=not traversalMode
            continue
            
        elif y==leny-1 and traversalMode:
            x+=1
            traversalMode=not traversalMode
            continue
        
        elif x==0 and traversalMode: 
            y+=1
            traversalMode=not traversalMode
            continue
        
        elif y==0 and not traversalMode:
            x+=1
            traversalMode=not traversalMode
            continue
        
        if traversalMode:
            x=x-1
            y=y+1
            
        else:
            y=y-1
            x=x+1
        
    return solution

array=[[1, 3, 4, 10], 
       [2, 5, 9, 11], 
       [6, 8, 12, 15], 
       [7, 13, 14, 16]]
print(zigzagTraverse(array))





