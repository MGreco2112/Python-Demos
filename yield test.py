def test():
    yield 1
    yield 2
    yield 3

#This appears to be how the range() function operates
for x in test():
    print(x)

#functionally identical to the range used to build range test
#further understanding of range() required to test without using range
def rangeTest(max):
    for x in range(max):
        yield x

for x in rangeTest(5):
    print(x)

#while loop implementation
#utilizing the while loop, I can simulate the range() function without calling it as in rangeTest()
# def whileRangeTest(max):
#     x = 0

#     while x < max:
#         yield x
#         x = x + 1

#redefine whileRangeTest with multiple parameters
def whileRangeTest(stop, start=None, step=None):
    x = 0
    increment = 1

    if (start != None):
        x = start
    
    if (step != None):
        increment = step

    while x < stop:
        yield x
        x = x + increment

for x in whileRangeTest(10, 5):
    print(x)

