#input phase
print("Please enter the part number.")
pn = input()
print("Please enter the quantity.")
qty = float(input())


#process phase
if pn == "10" or pn == "55":
    costpu = 1
else:
    if pn == "99":
        costpu = 2
    else:
        if pn == "80" or pn == "70":
            costpu = 3
        else:
            costpu = 5
total = qty * costpu


#output phase
print("For the part number #" + pn + " the cost per unit is:  $ " + str(costpu) + ", and the total cost is:  $ " + str(total))