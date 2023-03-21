#calculate the conversions from Farenheit to Celsius for 0 - 20 in a table

#print header for table
print(f"| Cel |  Far |")

#define loop in range to < 21
for cel in range(21):
    #formula for cel to far conversion
    far = (9/5 * cel) + 32

    #print formatted temps in table format
    print(f"| {cel:<3d} | {far:>2.1f} |")