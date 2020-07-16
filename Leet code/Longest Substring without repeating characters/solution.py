def longestSubstringWithoutDuplication(string):
	#window sliding
	if string=="":
        return string
    dict1={}
    dict1={x:0 for x in string}
    
    i=0
    j=0
    mi=0
    mj=0
    maxlen=0
	
    while i<len(string) and j<len(string):
        dict1[string[j]]+=1
        
        if dict1[string[j]]>1:
            dict1[string[j]]-=1
            j-=1
            dict1[string[i]]-=1
            i+=1
            
        if j-i>maxlen:
            maxlen=j-i
            mi=i
            mj=j
        j+=1
		
    return string[mi:mj+1]
