import textwrap

def wrap(string, max_width):
    output = ""
    
    for x in range(len(string)):
        if (x != 0 and x % max_width == 0):
            output += "\n"
    
        output += string[x]
        
    return output

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
