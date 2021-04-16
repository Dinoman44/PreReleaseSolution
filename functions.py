# function to get an integer as input, using recursive function
def get_int(string):
    x = input(string)
    try:
        return int(x)
    except ValueError:
        get_int(string)

# function to get a valid departing train time
def get_valid_up_time(timings):
    time = get_int("Train time: ")
    # makes sure that a train is present on the input time by referencing the timings
    while time not in timings:
        print("There is no train at this time. Choose another train")
        time = get_int("Train time: ")
    return time

# recursive function to get a valid down time
def get_valid_down_time(t1, timings):
    time = get_int("Train time: ")
    # makes sure that train is present on input time
    while time not in timings:
        print("There is no train at this time. Choose another train")
        time = get_int("Train time: ")
        # makes sure arrival is not before departure(only checks this when wrong time is given once)
        while time < t1:
            time = get_int("Train time: ")
    # if correct arrival time is given, but it is before departure time, function repeats, stopping only when arrival time is fully validated
    if time < t1:
        get_valid_down_time(t1, timings)

    return time
