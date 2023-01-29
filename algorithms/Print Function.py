if __name__ == '__main__':
    n = int(input())
    
    output = ""
    
    for x in range(n):
        if (x != 0):
            #str() casts int to string
            output += str(x)
    
    output += str(n)
    
    print(output)
