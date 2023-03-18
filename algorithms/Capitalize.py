#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    output = ""
    
    for character in range(len(s)):
        letter = s[character]
        
        if character == 0 or s[character - 1] == ' ':
            output += letter.upper()
        else :
            output += letter
        
    
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
