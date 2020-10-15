import math as m

def isSquare(number):
    x=int(m.sqrt(number))
    return True if pow(x,2)==number else False

def fibonacci_number(number):
    n1=5*pow(number,2)+4
    n2=5*pow(number,2)-4
    return "Yes" if isSquare(n1) or isSquare(n2) else "No"

print(fibonacci_number(4))