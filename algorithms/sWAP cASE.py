def swap_case(s):
    output = ""
    
    for x in s:
        if (x.isupper()):
            output += x.lower()
        else:
            output += x.upper()
    
    return output
