#Input phase
print("Please, enter the quantity of widgets.")
qty = float(input())

#Process phase
if qty > 10000:
    price = 10
else:
    if qty > 5000:
        price = 20
    else:
        price = 30
extprice = price * qty
tax = extprice * 0.07
total = extprice + tax

#Output phase
print("For " + str(qty) + " widget/s, the price is:  $ " + str(price) + ", therefore, the extended price is:  $ " + str(extprice))
print("Plus tax (7%):  $" + str(tax))
print("The total for the order is:  $ " + str(total))