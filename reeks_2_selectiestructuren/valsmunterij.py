weging1 = str(input())
weging2 = str(input())

def vindMuntstuk(weging):
    if(weging == "rechts"):
        return 1
    if(weging == "links"):
        return 2
    if(weging == "evenwicht"):
        return 3

print(f"muntstuk #{(vindMuntstuk(weging1) - 1) * 3 + vindMuntstuk(weging2)} is vervalst")
