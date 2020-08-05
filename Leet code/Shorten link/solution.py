def shortenPath(path):
	startsWithSlash= path[0]=="/"
	solution=[]
	if startsWithSlash:
		solution.append("")
	elements=path.split("/")
	for i in elements:
		if i!=".." and i!="" and i!=".":
			solution.append(i)
		elif i=="..":
			if len(solution)>0 and solution[-1]!="..":
				solution.pop()
			elif not startsWithSlash and len(solution)==0:
				solution.append("..")
			elif not startsWithSlash:
				solution.append("..")
	
	soln="/".join(solution)
	
	if len(solution)==1 and solution[-1]=="":
		return "/"
	
	if startsWithSlash and len(solution)==0:
		return "/"
	
	if startsWithSlash and soln[0]!="/":
		return "/"+soln
				
	return soln
