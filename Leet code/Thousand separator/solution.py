def printn(n):
    number=str(n)
    number=number[::-1]
    string=""
    for i in range(0,len(number),3):
        string+=number[i:i+3]
        string+='.'
    return string[0:len(string)-1][::-1]
    
print(printn(12345678))
