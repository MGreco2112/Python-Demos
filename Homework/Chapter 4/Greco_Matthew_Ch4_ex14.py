#write a program that uses a nested loop to print a cascading asterisk inverted pyramid

#initialize step_count var to 7 for counting asterisks in inner loop
step_count = 7

#define outer loop iterating 7 times through range
for level in range(7):
    #initialize output str var to "" to hold asterisks
    output = ""

    #define inner loop iterating for current value of step_count
    for points in range(step_count):
        #concatonate asterisk character to output str
        output += '*'

    #print output str left justified
    print(f"{output:<}")
    #decrement step_count var
    step_count -= 1