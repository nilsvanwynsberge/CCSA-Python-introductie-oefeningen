soort = str(input())
value = input()
antwoord = input()

def formule(soort, value, antwoord):
    if (soort == "kleur"):
        if (value != "rood"):
            if(antwoord == "ja"):
                return True
        if (value == "rood"):
            if(antwoord == "nee"):
                return True
    if (soort == "waarde"):
        if (int(value) % 2 == 0):
            if(antwoord == "ja"):
                return True
        if (int(value) % 2 == 1):
            if(antwoord == "nee"):
                return True 

print(f"Juist: kaarten met {soort} {value} moeten {'gedraaid worden' if antwoord == 'ja' else 'niet gedraaid worden'}." if (formule(soort, value, antwoord)) else f"Fout: kaarten met {soort} {value} moeten {'gedraaid worden' if antwoord == 'nee' else 'niet gedraaid worden'}.")