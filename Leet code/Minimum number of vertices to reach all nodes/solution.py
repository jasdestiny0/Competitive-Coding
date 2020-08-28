def print1(n, edges):
    numberOfLinks={i:0 for i in range(n)}
    links={i:[] for i in range(n)}
    for i in range(0,len(edges),1):
        numberOfLinks[edges[i][0]]=numberOfLinks[edges[i][0]]+1
        links[edges[i][0]]+=[edges[i][1]]
    
    bfs1=[[] for i in range(n)]
    for i in range(n):
        children=links[i]
        while len(children)>0:
            grandChildren=[]
            bfs1[i]+=children
            for j in children:
                grandChildren+=links[j]
            children=grandChildren.copy()
    
    bfs=[0 for i in range(n)]
    
    for i in range(n):
        bfs[i]=len(set(bfs1[i]))

    print(bfs)
    maxi=max(bfs)  
    sol=[]

    for i in range(n):
        if bfs[i]==maxi:
            sol.append(i)
    return sol, bfs, bfs1,links


print(print1(5,[[1,3],[2,0],[2,3],[1,0],[4,1],[0,3]]))
