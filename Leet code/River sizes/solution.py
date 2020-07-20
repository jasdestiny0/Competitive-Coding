def riverSizes(matrix):
    solution=[]
    checkpoint=[[True for i in range(len(matrix[0]))] for j in range(len(matrix))]
    for i in range(0, len(matrix[0]),1):
        for j in range(0,len(matrix),1):
            if matrix[j][i]==1:
                val=getSize(matrix,checkpoint,i,j,len(matrix[0])-1,len(matrix)-1,i,j)
                if val!=0:
                    solution.append(val)
    return solution

def getSize(matrix, checkpoint, fromx, fromy, limx, limy, x, y):
    if x>limx or y>limy or x<0 or y<0:
        return 0
    if matrix[y][x]==0 or not checkpoint[y][x]:
        return 0
    
    checkpoint[y][x]=False
    size=1

    size+=getSize(matrix,checkpoint, x,y, limx,limy, x-1,y)
    size+=getSize(matrix,checkpoint, x,y, limx,limy, x+1,y)
    size+=getSize(matrix,checkpoint, x,y, limx,limy, x,y-1)
    size+=getSize(matrix,checkpoint, x,y, limx,limy, x,y+1)
    
    return size
            
      
