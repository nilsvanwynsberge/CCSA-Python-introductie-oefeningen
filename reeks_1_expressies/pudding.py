aantal = int(input())
prijs = float(input())
stuksvoorcoupon = int(input())
mijlenpercoupon = int(input())

def berekeningPrijs(aantal, prijs):
    return aantal * prijs

def berekeningAantalMijlen(aantal, stkper, ffmper):
    coupons = aantal // stkper
    return coupons * ffmper

print(f"Phillips spendeerde ${berekeningPrijs(aantal, prijs)} voor {berekeningAantalMijlen(aantal, stuksvoorcoupon, mijlenpercoupon)} frequent flyer mijlen.")