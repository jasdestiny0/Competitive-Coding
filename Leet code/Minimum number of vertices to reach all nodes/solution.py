class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        pointed={i[1] for i in edges}
        pointer={i[0] for i in edges}
        p=pointer.copy()
        
        for i in pointer:
            if i in pointed:
                p.discard(i)
        
        return list(p)
        
        
        
