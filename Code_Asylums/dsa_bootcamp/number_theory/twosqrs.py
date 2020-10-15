import math as m
def twosqrs(number):
    s={}
    for i in range(0,number):
        if pow(i,2)> number:
            return "No"
        elif number-pow(i,2) in s:
            return "Yes"
        s[pow(i,2)]="True"
        
print(twosqrs(440929))