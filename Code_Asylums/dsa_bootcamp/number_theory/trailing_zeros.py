import math as m

def trailing_zeros(number):
    total=0
    cf=5
    current=m.floor(number/cf)
    while current!=0:
        total+=current
        cf*=5
        current=m.floor(number/cf)
    return total

print(trailing_zeros(20))
        
