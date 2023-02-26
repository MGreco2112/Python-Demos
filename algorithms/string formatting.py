def print_formatted(number):
    
    for x in range(1, number + 1):
        octal_num = str(oct(x))
        hex_num = str(hex(x))
        bin_num = str(bin(x))
        
        padding = len(bin(number)) - 2
        
        print(f"{x:>{padding}}", end=" ")
        print(f"{octal_num[2:len(octal_num)]:>{padding}}", end=" ")
        print(f"{hex_num.upper()[2:len(hex_num)]:>{padding}}", end=" ")
        print(f"{bin_num[2:len(bin_num)]:>{padding}}")
        
        
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)