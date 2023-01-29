# loop tutorial

#basic loop
for x in range(10):
    print(x)

#break line
print()

#index of string utilizing range for condition
word = "abcdefghij"

for x in range(10):
    print(word[x])

#break line
print()

#for in loop

for x in word:
    print(x)

#break line
print()

#iterate through array within loop
array = [1, 2, 3, 4, 5, 6, 6, 6, 8, 15]

for x in array:
    print(x)

#break line
print()

#adding logic to determine which elements are printed
for x in array:
    if (x % 2 == 0):
        print(x)


#break line
print()

