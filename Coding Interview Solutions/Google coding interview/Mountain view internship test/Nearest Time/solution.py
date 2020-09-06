import re

def solution(string):
    hours,minuites=[str(x) for x in string.split(':')]
    givenTime=hours+":"+minuites
    givenTime=givenTime.replace("?","\d")
    timeRegex=re.compile(r""+givenTime)
    solution=""
    upperValue=6 if string[3]=="?" else 10
    upperValue=4 if string[1]=="?" and string[0]=="2" else upperValue
    upperValue=3 if string[0]=="?" else upperValue
    for i in range(0,upperValue,1):
        if timeRegex.search(string.replace("?",str(i))):
            solution=string.replace("?",str(i))
            
    return solution
            

print(solution("1?:?8"))
print(convert(t.time()))
    
