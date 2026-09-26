array = []

while len(array) < 10:
    array.append(input())

def checksum(isbn):
   control = isbn.pop()
   total = 0
   for index, num in enumerate(isbn, start=1): 
      total += index * int(num)
   if total % 11 == int(control):
       return True
   return False

print("OK" if checksum(array) else "FOUT")