def topologicalSort(jobs, deps):
    preReqs={i:[] for i in jobs}
    lenPreReqs={i:0 for i in jobs}
    for i in deps:
        preReqs[i[1]]+=[i[0]]
        
    for i in preReqs.items():
        lenPreReqs[i[0]]=len(i[1])
    solution=[]
    print(preReqs)
    return solution

print(topologicalSort([1, 2, 3, 4],[[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]))