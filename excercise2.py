#write a program to assign a discount of 5% if ammount of purchases exceeds 1000
purchase = int (input ("Enter the total purchase: "))
if purchase >1000:
    discount = ((5/100)*purchase)
    print("Total discount = ",discount)
else:
    print ("No discount for goods worth 1000 or less!")