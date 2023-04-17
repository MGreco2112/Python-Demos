# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

list_A_string = input()
list_B_string = input()

list_A = []
list_B = []

for _ in list_A_string.split(" "):
    
    list_A.append(int(_))
    
for _ in list_B_string.split(" "):
    
    list_B.append(int(_))


print(product(list_A, list_B))