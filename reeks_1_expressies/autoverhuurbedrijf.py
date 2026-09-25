km_b = float(input())
km_e = float(input())
liter = float(input())

def kilometers(km_b, km_e):
    return km_e - km_b

def verbruik(km, liter):
    return liter / km * 100

print(verbruik(kilometers(km_b, km_e), liter))
