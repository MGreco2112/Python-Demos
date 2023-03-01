#length and width comparison
#ask user for length and width of two rectangles
#output which is larger

#define function with two parementers
def length_times_width(lent, widt):
    return lent * widt #return the value of the paremeters multiplied. This operation is the area of a rectangle formula

#inputs
length_one = float(input("Enter the length of the first rectangle: ")) #ask user for the length of a rectangle
width_one = float(input("Enter the width of the first rectangle: ")) #ask user for the width of a rectangle
length_two = float(input("Enter the length of the second rectangle: ")) #ask user for the length of a rectangle
width_two = float(input("Enter the width of the second rectangle: ")) #ask user for the width of a rectangle

#math operations on inputs
area_1 = length_times_width(length_one, width_one) #call the length_times_width function on rectangle one, store in area_1
area_2 = length_times_width(length_two, width_two) #call the length_times_with function on rectangle two, store in area_two

#comparison statements
if area_1 > area_2: #compare the value of area_1 and area_2, if area_1 is larger
    print("Rectangle 1 has a larger area than Rectangle 2") #print that rectangle 1 has a larger area
else: #otherwise
    print("Rectangle 2 has a larger area than Rectangle 1") #print that rectangle two has a larger area