# cook your dish here
string=str(input())
n,testcases=[int(x) for x in string.split(' ')]
firstNumber=n+2
lastNumber=3*n
mid=(firstNumber+lastNumber)/2
for testcase in range(testcases):
    number=int(input())
    if number<firstNumber or number>lastNumber:
        print(0)
    elif number<mid:
        print(number-firstNumber+1)
    else:
        print(lastNumber-number+1)
        
    
    
