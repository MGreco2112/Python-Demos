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
