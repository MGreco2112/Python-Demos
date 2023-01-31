def count_substring(string, sub_string):
    output = 0
    
    for x in range(len(string) - len(sub_string) + 1):
        
        stub = ""
        for y in range(x, x+len(sub_string)):
            stub +=string[y]
    
        
        if (stub == sub_string):
            output += 1
    
    return output
