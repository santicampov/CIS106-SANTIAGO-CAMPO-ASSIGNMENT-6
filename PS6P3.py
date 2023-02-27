#input phase
print("Enter the principle amount of the CD.")
prin = float(input())
print("Please enter the year to maturity.")
year = float(input())

#process phase
if prin > 100000 and year == 5:
    rate = 0.06
else:
    if prin > 50000 and year == 10:
        rate = 0.05
    else:
        if prin > 50000 and year == 5:
            rate = 0.04
        else:
            rate = 0.02
interest = prin * rate

#output phase
print("For the principle of $ " + str(prin) + ", for the first year, the interest rate is: " + str(rate) + ". and the interest amount for the first year is: $ " + str(interest))