def totalNumberOfWays(string,ways=[1]):
        if len(string)==0 or string[0]=='0':
                return 0
        if isSplit(string):
                totalNumberOfWays(string[2:])
                ways[0]+=1
        totalNumberOfWays(string[1:])
        return ways[0]

def isSplit(string):
        if len(string)<2:
                return False
        if int(string[0:2])>26 or int(string[0:2])<1 or string[1]=='0':
                return False
        print(string)
        return True
        

print(totalNumberOfWays("011"))


