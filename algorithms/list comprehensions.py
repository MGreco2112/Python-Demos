if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    output = []
    
    for outer in range(x + 1):
        for middle in range(y + 1):
            for inner in range(z + 1):
                if outer + middle + inner != n:
                    output.append([outer, middle, inner])
    
    print(output)
