def getLowestCommonManager(topManager, reportOne, reportTwo):
    	sol=[]
	helper(topManager, reportOne, reportTwo, 0, sol)
	return sol[-1]
	
def helper(node, reportOne, reportTwo, current, sol):
	if node==reportOne or node==reportTwo:
		current+=1
	for i in node.directReports:
		current+=helper(i, reportOne, reportTwo, 0, sol)
	if sol:
		return current
	if current==2:
		sol.append(node)	
	return current

class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
