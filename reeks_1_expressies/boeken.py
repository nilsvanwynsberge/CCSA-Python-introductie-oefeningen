
def boekFunc(amount, price, discountrate):
    boekKost = amount * price * (1 - discountrate) 
    verzendKost = 3 + ((amount - 1) * 0.75)  
    return boekKost + verzendKost

print(boekFunc(60, 24.95, 0.4)); 