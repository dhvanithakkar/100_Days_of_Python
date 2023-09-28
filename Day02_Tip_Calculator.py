#If the bill was $150.00, split between 5 people, with 12% tip.
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
no_of_people = int(input("How many people to split the bill? "))
tip_percentage = float(
    input("What percentage tip would you like to give? 10, 12, or 15? "))
#Each person should pay (150.00 / 5) * 1.12 = 33.6
per_person = (total_bill / no_of_people) * (1 + (tip_percentage / 100))
#or use round(per_person, 2) to round off till 2 decimal places. this will give 11.4 for 11.4
print(f"Each person should pay: ${per_person:.2f}") #this will give 11.40 for 11.4
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#format(math.pi, '.12g')  # give 12 significant digits - '3.14159265359'
#format(math.pi, '.2f')   # give 2 digits after the point - '3.14'

"""
Some print formatting:
>>> a = 13.946
>>> print(a)
13.946
>>> print("%.2f" % a)
13.95
>>> round(a,2)
13.949999999999999
>>> print("%.2f" % round(a, 2))
13.95
>>> print("{:.2f}".format(a))
13.95
>>> print("{:.2f}".format(round(a, 2)))
13.95
>>> print("{:.15f}".format(round(a, 2)))
13.949999999999999

"""