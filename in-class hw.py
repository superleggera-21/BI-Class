
    # Define a function called hotel_cost with one argument days as user input. 
    # The hotel costs $140 per day. So, the function hotel_cost should return 140 * days.
def hotel_cost(x):
    return 140*x

    # Define a function called plane_ride_cost that takes a string, city, as user input. 
    # The function should return a different price depending on the location, similar to the code example above. 
    # Below are the valid destinations and their corresponding round-trip prices."Charlotte": 183 "Tampa": 220 "Pittsburgh": 222 "Los Angeles": 475
def plane_ride_cost(city):
    citydict = {"Charlotte": 183, "Tampa": 220, "Pittsburgh": 222, "Los Angeles": 475}
    return citydict[city]

    # Below your existing code, define a function called rental_car_cost with an argument called days. 
    # Calculate the cost of renting the car: Every day you rent the car costs $40.
    # (cost=40*days) if you rent the car for 7 or more days, you get $50 off your total(cost-=50). 
    # Alternatively (elif), if you rent the car for 3 or more days, you get $20 off your total. 
    # You cannot get both of the above discounts. Return that cost.
def rental_car_cost(days):
    if days >= 7:
        cost = 40*days-50
        return cost
    elif days >=3:
        cost = 40*days-20
        return cost
    else:
        cost = 40*days
        return cost

    # Then, define a function called trip_cost that takes two arguments, city and days. 
    # Like the example above, have your function print the sum of calling the rental_car_cost(days), 
    # hotel_cost(days), and plane_ride_cost(city) functions.
def trip_cost(city, days):
    cost = plane_ride_cost(city)+rental_car_cost(days)+hotel_cost(days)
    print('The total cost of the trip is '+str(cost)+' dollars.')

    # Modify your trip_cost function definition. Add a third argument, spending_money (also a user input). 
    # Modify what the trip_cost function does. Add the variable `spending_money to the sum that it prints.
def trip_cost_with_spending(city, days, spending_money):
    cost = plane_ride_cost(city)+rental_car_cost(days)+hotel_cost(days)+spending_money
    print('The total cost of the trip is '+str(cost)+' dollars.')

trip_cost_with_spending('Tampa',21,1200)


def trip_cost_with_spending_manual():
    city = input('Which city are you going?')
    days = int(input('How many days will the vacation be?'))
    spending_money = int(input('How much money will you bring?'))
    cost = plane_ride_cost(city)+rental_car_cost(days)+hotel_cost(days)+spending_money
    print('The total cost of the trip is '+str(cost)+' dollars.')

trip_cost_with_spending_manual()