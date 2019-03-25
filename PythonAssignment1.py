# 1. Planting Grapevines

# A vineyard owner is planting several new rows of grapevines, and needs to know how many grapevines to plant in each row. 
# She has determined that after measuring the length of a future row, 
# she can use the following formula to calculate the number of vines that will fit in the row, 
# along with the trellis end-post assemblies that will need to be constructed at each end of the row:

# V = (R - 2E) / S

# The terms in the formula are:
#     V is the number of grapevines that will fit in the row.
#     R is the length of the row, in feet.
#     E is the amount of space, in feet, used by an end-post assembly.
#     S is the space between vines, in feet.

# Write a program that makes the calculation for the vineyard owner. The program should ask the user to input the following:
#     The length of the row, in feet
#     The amount of space used by an end-post assembly, in feet
#     The amount of space between the vines, in feet

# Once the input data has been entered, the program should calculate and display the number of grapevines that will fit in the row.
def calculator():
    r = float(input('Please enter the length of the row, in feet: '))
    e = float(input('Please enter the amount of space, in square feet: '))
    s = float(input('Please enter the speace between the vines, in feet: '))
    res = (r-2*e)/s
    if res > 0:
        print('You can fit '+str(res)+' grapevines to fill the row.')
    else:
        print('You can\'t fit any vines in the row!')
calculator()

# 2. Age Classifier

# Write a program that asks the user to enter a person’s age. 
# The program should display a message indicating whether the person is an infant, a child, a teenager, or an adult. 
# Following are the guidelines:

#     If the person is 1 year old or less, he or she is an infant.
#     If the person is older than 1 year, but younger than 13 years, he or she is a child.
#     If the person is at least 13 years old, but less than 20 years old, he or she is a teenager.
#     If the person is at least 20 years old, he or she is an adult.
def age_classifier():
    age = input('What is your age? ')
    if age >= 20:
        print('You are an adult!')
    elif age >= 13:
        print('You are a teenager!')
    elif age >= 1:
        print('You are a child!')
    else:
        print("You are an infant!")
age_classifier
# 3. Write a program with a loop that asks the user to enter a series of positive numbers. 
# The user should enter a negative number to signal the end of the series.
# After all the positive numbers have been entered, the program should display their sum
def looper():
    x = 1
    while x > 0:
        x = int(input('Please enter a number'))

looper()
# 4. Write a program that calculates the amount of money a person would earn over a
# period of time if his or her salary is one penny the first day, two pennies the second day, 
# and continues to double each day. The program should ask the user for the number of days.
# Display a table showing what the salary was for each day, then show the total pay at the end of the period.
# The output should be displayed in a dollar amount, not the number of pennies.
def earncalc(days):
    day = 1
    total = 0
    pay = 1
    for i in range(days):
        print('day '+str(day)+' paid '+str(float(pay)/100))
        day += 1
        total += pay
        pay *= 2
    print("the total paid amount is"+str(total))

            

earncalc(100)
# 5. Write a program that uses nested loops to collect data
#  and calculate the average rainfall over a period of years. 
#  The program should first ask for the number of years. 
#  The outer loop will iterate once for each year.
#  The inner loop will iterate twelve times, once for each month. 
#  Each iteration of the inner loop will ask the user for the inches of rainfall for that month. 
#  After all iterations, the program should display the number of months, 
#  the total inches of rainfall, and the average rainfall per month for the entire period.
def rainfall():
    yrs = input("how many years of rainfall data do you have? ")
    total = 0
    for i in range(int(yrs)):
        for k in range(12):
            rain = input("How big was the rainfall for month "+str(k+1)+", year "+str(i+1)+" (in inches)?")
            total += float(rain)
    avg = total/(int(yrs)*12)
    print("The total rainfall is "+str(total)+" inches, and the average rainfall per month is "+str(avg)+" inches.")

rainfall()