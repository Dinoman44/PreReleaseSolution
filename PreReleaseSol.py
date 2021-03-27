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

# defines basic error checking for the input times and passengers
def errorChecking(tickets, timings, time):
    # time is passed in as input, and timings is an array with the valid times
    while time not in timings:
        print("No train at this time. Choose another time")
        time = int(input("Train time: "))

    # gets number of passengers as input, making sure its between 1 and 80
    numPeople = int(input("No. of Passengers: "))
    while numPeople > 80 or numPeople < 1:
        print("Min 1, max 80 passengers per group")
        numPeople = int(input("No. of passengers: "))

    # if x = [1, 2, 3, 4] then x.index(3) returns the index of the value 3 in the array x
    while tickets[timings.index(time)] < numPeople:
        print("Not enough seats. Choose another train")
        time = int(input("Train time: "))
        while time not in timings:
            print("No train at this time. Choose another time")
            time = int(input("Train time: "))

    # once error checking is complete, it returns the number of passengers and the train time in an array
    return [numPeople, time]

x = True
while x:
    print("")
    upTime = int(input("Time for up train: "))
    arr = errorChecking(ticketsLeft[:4], upTimes, upTime)
    numPassengers, upTime = arr[0], arr[1] # assigns the number of passengers and the timing for up train
    downTime = int(input("Time for down train: "))
    while downTime < upTime:
        print("Cannot time travel. Choose a later train")
        downTime = int(input("Time for down train: "))
    downTime = errorChecking(ticketsLeft[4:], downTimes, downTime)[1] # assigns the timing for down train

    print("")
    # gets some index values(by using .index())
    i1 = upTimes.index(upTime)
    i2 = downTimes.index(downTime) + 4
    # subtracts the number of tickets remaining and adds the number of passengers travelling
    ticketsLeft[i1] -= numPassengers
    ticketsLeft[i2] -= numPassengers # a -= b is the same as a = a - b
    peoplePerTrain[i1] += numPassengers # a += b is the same as a = a + b
    peoplePerTrain[i2] += numPassengers
    # calculates the price and adds it to the money collected per train
    # x // y returns the quotient of x /y (so 9 // 10 returns 0), accounting for the discount by making sure its in range
    priceUp = (25 * numPassengers) - (25 * (numPassengers // 10))
    priceDown = priceUp
    moneyPerTrain[i1] += priceUp
    moneyPerTrain[i2] += priceDown
    # f-strings to put variables into strings
    print(f"Cost of up journey: ${priceUp:,.2f}")
    print(f"Cost of down journey: ${priceDown:,.2f}")
    print(f"Total cost: ${(priceUp + priceDown):,.2f}")

    print("\n| Train times | Direction | Tickets left |")
    for i in range(4):
        print(f"|     {upTimes[i]}:00   |    Up     |      {ticketsLeft[i]}     |")
        print(f"|     {downTimes[i]}:00   |   Down    |      {ticketsLeft[i+4]}     |")

    while True:
        x = input("Do you want to buy tickets? [y/n]\n") # "\n" goes to the next line
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