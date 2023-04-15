# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

output = 0

shoes = int(input())

sizes = Counter(list(input()))

customers = int(input())

for _ in range(customers):
    order = input().split(' ')
    
    shoe_size = order[0]
    shoe_price = int(order[1])
    
    if shoe_size in Counter(sizes).keys():
        output += shoe_price
        sizes[shoe_size] -= 1
        shoes -= 1
        
        
print(output)