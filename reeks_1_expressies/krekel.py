aantal = float(input())

def tempC(aantal):
   return 10 + (aantal - 40) / 7
def tempF(aantal):
   return 50 + (aantal - 40) / 4

print("temperatuur (Fahrenheit): " + str(tempF(aantal)))
print("temperatuur (Celsius): " + str(tempC(aantal)))
