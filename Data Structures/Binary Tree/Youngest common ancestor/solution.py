# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, d1, d2):
	depth1=getDepth(d1,topAncestor)
	depth2=getDepth(d2,topAncestor)
	
	if depth1-depth2>0:
		return findCommonAncestor(d1, d2, depth1-depth2)
	else:
		return findCommonAncestor(d2,d1,depth2-depth1)
	
def findCommonAncestor(d1,d2,diff):
	while diff>0:
		d1=d1.ancestor
		diff-=1
	while d1!=d2:
		d1=d1.ancestor
		d2=d2.ancestor
	return d1
	
	
def getDepth(descendant, topAncestor):
	count=0
	while descendant!= topAncestor:
		count+=1
		descendant=descendant.ancestor
	return count
	
	
			
		
