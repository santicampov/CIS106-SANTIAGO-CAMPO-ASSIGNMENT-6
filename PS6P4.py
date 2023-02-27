#input phase
print("Please enter the number of tickets.")
qty = float(input())


#process phase
if qty >= 25:
    ppt = 50
else:
    if qty >= 10:
        ppt = 60
    else:
        if qty >= 5:
            ppt = 70
        else:
            ppt = 75
total = qty * ppt


#output phase
print("For " + str(qty) + " tickets. the price per ticket is:  $ " + str(ppt) + ".  And the total cost is:  $ " + str(total))