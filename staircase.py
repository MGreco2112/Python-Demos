def staircase(n):
    #pointer indicates how many # to concactonate to output
    pointer = n - 1
    
    for x in range(n):
        #output is output string
        output = ""
        for y in range(n):
            #if y is greater than or equal to pointer value, that indicates how many # to print
            if (y >= pointer):
                output += "#"
        #format output to the right in a field of width n
        print(f"{output:>{n}}")
        #decrement pointer to allocate more #'s into output
        pointer = pointer - 1
