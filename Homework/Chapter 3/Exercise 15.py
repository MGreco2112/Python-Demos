#Time calculator
#ask user to input a number of seconds
#if the time is under a minute, print that time in seconds
#else if time is over a minute but less than an hour, print time in minutes and seconds
#else if time is over an hour, print that time in hours and minutes and seconds
#else if time is over a day, print that time in days and hourse and minutes and seconds
#60 seconds in a minute
#3,600 seconds in an hour
#86,400 seconds in a day

#initialize four constants
MINUTE_IN_SECONDS = 60 #one minute is 60 seconds
HOUR_IN_SECONDS = 3600 #one hour is 3600 seconds
DAY_IN_SECONDS = 86400 #one day is 86400 seconds
MINIMUM_WITHOUT_PADDING = 10 #minimum number that will not need leading zeroes added for formatting

#Ask user for an input of seconds
input_seconds = int(input("Enter a number of seconds: "))

if input_seconds < MINUTE_IN_SECONDS: #check value of input_seconds, if less than MINUTE_IN_SECONDS enter block
    print(f"{input_seconds} second(s)") #print value of input_seconds

elif input_seconds >= MINUTE_IN_SECONDS and input_seconds < HOUR_IN_SECONDS: #check value of input_seconds for values less or equal to MINUTE_IN_SECONDS or less than DAY_IN_SECONDS
    minutes = int(input_seconds / MINUTE_IN_SECONDS)#store input_seconds dividied by MINUTE_IN_SECONDS as an int, cutting off any fractional seconds outside of 1 minute
    seconds = input_seconds - (minutes * MINUTE_IN_SECONDS)#multiply the numer of minutes by MINUTE_IN_SECONDS, subtract that from input_seconds to get remaining seconds

    if seconds < MINIMUM_WITHOUT_PADDING: #conditional to determine if leading zero needs to be added to seconds for formatting
        seconds = "0" + str(seconds) #update value of seconds to a string containing a leading zero to pad out 10s place
    else:
        seconds = str(seconds) #format seconds as a string for display consistency

    print(f"{minutes}:{seconds} minute(s)") #print minutes and seconds in time ':' formatting

elif input_seconds >= HOUR_IN_SECONDS and input_seconds < DAY_IN_SECONDS: #check value of input_seconds, if less than DAY_IN_SECONDS enter block
    hours = int(input_seconds / HOUR_IN_SECONDS)#store input_seconds dividied by HOUR_IN_SECONDS as an int
    input_seconds -= hours * HOUR_IN_SECONDS#reduce input_seconds by number of hours multiplied by seconds per hour
    minutes = int(input_seconds / MINUTE_IN_SECONDS)#store reduced input_seconds divided by MINUTE_IN)SECONDS as an int
    seconds = input_seconds - (minutes * MINUTE_IN_SECONDS)#store input_seconds reduced by the value of minutes times MINUTE_IN_SECONDS

    if minutes < MINIMUM_WITHOUT_PADDING:#if minutes is lower than a 10s value
        minutes = "0" + str(minutes)#parse minutes as a string and append a 0 character to the front
    else:
        minutes = str(minutes)#otherwise parse minutes as a string for consistency
    
    if seconds < MINIMUM_WITHOUT_PADDING:#if seconds is lower than a 10s value
        seconds = "0" + str(seconds)#parse seconds as a string and append a 0 character to the front
    else:
        seconds = str(seconds)#otherwise parse seconds as a string for consistency
    
    print(f"{hours}:{minutes}:{seconds} hour(s)")#print hours and minutes and seconds in time ':' formatting

else: #if seconds is greater or equal to DAY_IN_SECONDS
    days = int(input_seconds / DAY_IN_SECONDS)#store input_seconds divided by DAY_IN_SECONDS as an int
    input_seconds -= days * DAY_IN_SECONDS#reduce input_seconds by days multiplied by DAY_IN_SECONDS
    hours = int(input_seconds / HOUR_IN_SECONDS)#store reduced input_seconds divided by HOUR_IN_SECONDS as an int
    input_seconds -= hours * HOUR_IN_SECONDS#reduce input_seconds by hours times HOUR_IN_SECONDS
    minutes = int(input_seconds / MINUTE_IN_SECONDS)#store reduced input_seconds divided by MINUTE_IN_SECONDS as an int
    seconds = input_seconds - (minutes * MINUTE_IN_SECONDS)#store input_seconds reduced by minutes times MINUTE_IN_SECONDS as an int

    if hours < MINIMUM_WITHOUT_PADDING:#if hours is lower than a 10s value
        hours = "0" + str(hours)#parse hours as a string and append a 0 character to the front
    else:
        hours = str(hours)#otherwise parse hours as a string for consistency

    if minutes < MINIMUM_WITHOUT_PADDING:#if minutes is lower than a 10s value
        minutes = "0" + str(minutes)#parse minutes as a string and append a 0 character to the front
    else:
        minutes = str(minutes)#otherwise parse as a string for consistency
    
    if seconds < MINIMUM_WITHOUT_PADDING:#if seconds is lower than a 10s value
        seconds = "0" + str(seconds)#parse seconds as a string and append a 0 character to the front
    else:
        seconds = str(seconds)#otherwise parse as a string for consistency
    
    print(f"{days}:{hours}:{minutes}:{seconds} day(s)")#print days and hours and minutes and seconds in time ':' formatting

