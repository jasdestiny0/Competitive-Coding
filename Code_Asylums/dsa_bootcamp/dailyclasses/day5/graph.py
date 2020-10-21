class graph:
    def __init__(self, x={}, v=0):
        self.value=x
        self.vertices=v
    
    def ratTraverse(self, posX, posY, grid, destX=3, destY=3):
        print(posX, posY)
        if destX==posX and destY==posY:
            print("possible")
            return True
        
        if grid[posY][posX]==0 or posX>=len(grid(-1)) or posY>=len(grid):
            return False

        r=self.ratTraverse(posX+1, posY, grid, destX, destY)
        d=self.ratTraverse(posX, posY+1, grid, destX, destY)
        l=self.ratTraverse(posX-1, posY, grid, destX, destY)
        u=self.ratTraverse(posX, posY-1, grid, destX, destY)

        if u or d or l or u:
            print("not possible")
        return False
            

g=graph()
print(g.ratTraverse(0,0,[
[1,0,1,0],
[1,1,0,0],
[1,0,1,0],
[1,1,1,1]
],-1,-1))

    
