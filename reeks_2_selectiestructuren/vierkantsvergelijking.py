import math

a = float(input())
b = float(input())
c = float(input())

def berekenWortels(a, b, c):
    sol = b*b - 4*a*c
    array = []
    if (sol < 0):
        array.append("geen")
        return array
    if (sol == 0):
        array.append("een")
        array.append(-b/(2*a))
        return array
    array.append("twee")
    sol1 = (-b - math.sqrt(sol))/ (2*a)
    sol2 = (-b + math.sqrt(sol))/ (2*a)
    
    array.append(min(sol1, sol2))
    array.append(max(sol1, sol2))
    return array

answer = berekenWortels(a, b, c)
print(answer[0] + " wortels" if len(answer) != 2 else answer[0] + " wortel")
if len(answer) > 1: 
    print(answer[1])
if len(answer) > 2: 
    print(answer[2])
