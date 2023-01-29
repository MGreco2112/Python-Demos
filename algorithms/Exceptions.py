
queries = int(input())

for x in range(queries):
    unparsedQuery = input()
    
    
    try:
        a = int(unparsedQuery[0])
        b = int(unparsedQuery[2])
        print(a//b)
        #except ${ExceptionType} as ${variable}
    except ValueError as e:
        print("Error Code:", e)
    except ZeroDivisionError as e:
        print("Error Code:", e)
