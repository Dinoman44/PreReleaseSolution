from functions import get_int, get_valid_up_time, get_valid_down_time
# Task 1

# in the first 3 arrays, the first 4 indexes correspond to each of the up times, and the last 4 indexes correspond to each of the down times
peoplePerTrain = [0, 0, 0, 0, 0, 0, 0, 0]
ticketsLeft = [480, 480, 480, 480, 480, 480, 480, 640]
moneyPerTrain = [0, 0, 0, 0, 0, 0, 0, 0]
upTimes = [9, 11, 13, 15]
downTimes = [10, 12, 14, 16]

print("| Train times | Direction | Tickets left |")
for i in range(4):
    print(f"|     {upTimes[i]}:00   |    Up     |      {ticketsLeft[i]}     |")
    print(f"|     {downTimes[i]}:00   |   Down    |      {ticketsLeft[i+4]}     |")

# Task 2
x = True
while x:
    # gets the number of passengers, making sure its between 1 and 80
    numPassengers = get_int("\nNo. of passengers: ")
    while numPassengers < 1 or numPassengers > 80:
        print("Min. 1, max 80 passengers per group")
        numPassengers = get_int("No. of passengers: ")

    # gets a valid time for the departing train
    print("[For departure/up train]")
    upTime = get_valid_up_time(upTimes)
    while ticketsLeft[upTimes.index(upTime)] < numPassengers:
        print("Not enough seats. Choose a different time")
        upTime = get_valid_time(upTimes)

    # gets a valid time for the arriving train
    print("\n[For arrival/down train]")
    downTime = get_valid_down_time(upTime, downTimes)
    while ticketsLeft[downTimes.index(downTime)] < numPassengers:
        print("Not enough seats. Choose a different time")
        downTime = get_valid_down_time(upTime, downTimes)

    # gets some index values(by using .index())
    i1 = upTimes.index(upTime)
    i2 = downTimes.index(downTime) + 4
    # subtracts the number of tickets remaining and adds the number of passengers travelling
    peoplePerTrain[i1] += numPassengers
    peoplePerTrain[i2] += numPassengers
    ticketsLeft[i1] -= numPassengers
    ticketsLeft[i2] -= numPassengers
    # calculates the price and adds it to the money collected per train
    # x // y returns the quotient of x/y (so 9 // 10 returns 0), accounting for the discount by making sure its in range
    costUp = (25 * numPassengers) - (25 * (numPassengers // 10))
    costDown = costUp
    moneyPerTrain[i1] += costUp
    moneyPerTrain[i2] += costDown
    # f-strings to put variables into strings, with :,.2f to format the string to use commas and 2 decimal places(ex: 1,000.00)
    print(f"Cost for departing train: $ {costUp:,.2f}")
    print(f"Cost for arriving train: $ {costDown:,.2f}")
    print(f"Total cost: $ {(costUp + costDown):,.2f}")

    # display the train times table again
    print("\n| Train times | Direction | Tickets left |")
    for i in range(4):
        print(f"|     {upTimes[i]}:00   |    Up     |      {ticketsLeft[i]}     |")
        print(f"|     {downTimes[i]}:00   |   Down    |      {ticketsLeft[i+4]}     |")

    while True:
        x = input("\nDo you want to buy tickets? [y/n]")
        if x == "y":
            break
        elif x == "n":
            x = False
            break

# Task 3
print("| Train times | No. of Passengers | Money collected |")
for i in range(4):
    print(f"| {upTimes[i]}:00 | {peoplePerTrain[i]} | ${moneyPerTrain[i]:,.2f} |")
    print(f"| {downTimes[i]}:00 | {peoplePerTrain[i+4]} | ${moneyPerTrain[i+4]:,.2f} |")

# sum() function returns the sum of the arguments(sum(1, 2, 3) returns 6, and sum([3, 4, 5, 0]) returns 12)
print(f"Total no. of passengers = {sum(peoplePerTrain)}")
print(f"Total money collected = ${sum(moneyPerTrain):,.2f}") # :,.2f makes sure the number has 2 decimal places and commas after every 3 digits
# max() function returns the highest value among the given arguments(similar to sum())
maxPeople = max(peoplePerTrain)
i = peoplePerTrain.index(maxPeople) # get index of the highest value
if i < 4:
    time = upTimes[i]
else:
    time = downTimes[i-4]
print(f"Train with most passengers - {time}:00 train({maxPeople} passengers)")
