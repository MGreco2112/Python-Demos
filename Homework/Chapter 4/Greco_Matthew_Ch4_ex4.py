#calculate distance traveled per hour based on user input
#take user input of speed of vehicle in mph
#take input for how many hours of travel time

#iterate loop for hours, multiply speed by loop iteration
#print hour | distance inside each iteration

#take user input for speed in MPH
speed = int(input("Enter the speed in MPH: "))

#take user input for travel time
time = int(input("Enter the length of travel in hours: "))

#print header for table
print(f"| HOUR " + "|" + " DISTANCE TRAVELLED |")

#define loop for range starting at 1 and running until counter is less than time plus 1
for hour in range(1, time + 1):
    #distance var holds travel speed times current loop iteration for hour
    distance = hour * speed

    #print hour | distance formatted to fit within table size definitions neatly
    print(f"| {hour:<4d} | {distance:>18d} |")
