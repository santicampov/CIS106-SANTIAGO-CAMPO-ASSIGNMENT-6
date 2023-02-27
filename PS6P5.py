#input phase
print("Please enter your last name.")
lname = input()
print("Please enter your salary.")
salary = float(input())
print("Please enter your job level.")
jl = float(input())


#process phase
if jl >= 10:
    brate = 0.25
else:
    if jl >= 5:
        brate = 0.2
    else:
        brate = 0.1
bonus = salary * brate


#output phase
print("For " + lname + " the bonus is:   $ " + str(bonus))