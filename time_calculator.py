def add_time(t1, t2, dow=None):

    """Input: t1 = start time, t2 = time to add, day = day of the week
    Output: new time, day of the week, and number of days passed
    t1 should be in 12 hour HH:MM AM/PM format 
    t2 should be in 24 hour HH:MM format
    Day shopuld be a full DOW string, case insensitive"""

    days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    t1 = t1.replace(" ", ":")

    t1_split = t1.split(":")
    t2_split = t2.split(":")

    # basic math addition before converting to 12 hour time
    new_hour = int(t1_split[0]) + int(t2_split[0])
    new_minute = int(t1_split[1]) + int(t2_split[1])

    # if minues > 60, add 1 to hour and subtract 60 from minutes
    while new_minute >= 60:
        new_hour += 1
        new_minute -= 60

    # add leading 0 to minutes if needed
    new_minute = str(new_minute)
    if len(new_minute) == 1:
        new_minute = "0" + new_minute    

    am_pm = t1_split[2]
    if not dow:
        day_count = 0
        while new_hour >= 12:
            new_hour -= 12
            if am_pm == "AM":
                am_pm = "PM"
            else:
                am_pm = "AM"
                day_count += 1

    else:
        day_count = 0
        dow = dow.lower()
        day = days_of_week.index(dow)
        while new_hour >= 12:
            new_hour -= 12
            if am_pm == "AM":
                am_pm = "PM"
            else:
                am_pm = "AM"
                day_count += 1
                day += 1

            
        day = days_of_week[day % 7]

    # convert hour to 12 hour time
    if new_hour == 0:
        new_hour = 12

    #construct new time string
    new_time = ""
    # base case, no day of week and no days passed
    if not dow and day_count == 0:
        new_time = f"{new_hour}:{new_minute} {am_pm}"
    # case with day of week and no days passed
    elif dow and day_count == 0:
        new_time = f"{new_hour}:{new_minute} {am_pm}, {day.capitalize()}"
    # case with no day of week and 1 day passed
    elif not dow and day_count == 1:
        new_time = f"{new_hour}:{new_minute} {am_pm} (next day)"
    # case with day of week and 1 day passed
    elif dow and day_count == 1:
        new_time = f"{new_hour}:{new_minute} {am_pm}, {day.capitalize()} (next day)"
    # case with no day of week and multiple days passed
    elif not dow and day_count > 1:
        new_time = f"{new_hour}:{new_minute} {am_pm} ({day_count} days later)"
    # case with day of week and multiple days passed
    else:
        new_time = f"{new_hour}:{new_minute} {am_pm}, {day.capitalize()} ({day_count} days later)"


    return new_time
