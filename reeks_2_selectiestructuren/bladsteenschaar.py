def bepaalWinnaar(player1, player2): 
    if (player1 == player2):
        return 0
    if (player1 == "schaar"):
        if (player2 == "hagedis" or player2 == "blad"):
            return 1
    if (player1 == "blad"):
        if (player2 == "steen" or player2 == "Spock"):
            return 1
    if (player1 == "steen"):
        if (player2 == "schaar" or player2 == "hagedis"):
            return 1
    if (player1 == "hagedis"):
        if (player2 == "Spock" or player2 == "blad"):
            return 1
    if (player1 == "Spock"):
        if (player2 == "schaar" or player2 == "steen"):
            return 1
    return 2

user1 = input("Speler 1, geef je keuze: ")
user2 = input("Speler 2, geef je keuze: ")

winnaar = bepaalWinnaar(user1, user2)
print(f"speler{str(winnaar)} wint" if winnaar > 0 else "gelijkspel")


