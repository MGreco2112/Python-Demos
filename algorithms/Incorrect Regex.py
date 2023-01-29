import re
#import the Regex Library

queries = int(input())

for x in range(queries):
    check = input()
    
    try:
        #Attempt to compile the check var into a regex
        re.compile(check)
        print(True)
    except re.error:
        #if compile fails, throw exception
        print(False)
