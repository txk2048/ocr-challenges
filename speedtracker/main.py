import math

# time1 and time2 are in seconds
# distance is in miles
# return average speed in mph
def calculate_speed(time1, time2, distance):
    # convert time1 and time2 to hours
    time1 /= 60 ** 2
    time2 /= 60 ** 2

    return math.floor(distance / (time2 - time1))
