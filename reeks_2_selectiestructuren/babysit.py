uur1 = int(input())
min1 = int(input())
uur2 = int(input())
min2 = int(input())

def tijdsberekening(uur, min):
    if (uur == 0): uur = 24
    tijd = uur + (min / 60)
    return tijd

tijd1 = float(tijdsberekening(uur1, min1))
tijd2 = float(tijdsberekening(uur2, min2))

def tijdscontrole(tijd):
    if(tijd < 18 or tijd > 24):
        return -1
    return tijd

def kostberekening(tijd1, tijd2):
    if(tijd1 == -1 or tijd2 == -1): return "ongeldige invoer"
    if (tijd2 < 21.5):
        return (tijd2 - tijd1) * 2
    if (tijd1 > 21.5):
        return (tijd2 - tijd1) * 4
    return (21.5 - tijd1) * 2 + (tijd2 - 21.5) * 4

print(kostberekening(tijdscontrole(tijd1), tijdscontrole(tijd2)))
    

