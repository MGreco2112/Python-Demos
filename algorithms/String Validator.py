if __name__ == '__main__':
    s = input()
    
    #initialize boolean variables to hold conditions based on characters in String s, initlze to False
    is_alnum = False
    is_alpha = False
    has_digits = False
    has_lower = False
    has_upper = False
    
    
    #iterate through each character in string s
    for ch in s:
        if is_alnum == False and ch.isalnum(): #test if current character is alpha numeric
            is_alnum = True #set bool to True if condition is encountered
        
        if is_alpha == False and ch.isalpha(): #test if current character is alphabetical character
            is_alpha = True #set bool to True if condition is encountered
        
        if has_digits == False and ch.isdigit(): #test if current character is digit
            has_digits = True #set bool to True if condition is encountered
            
        if has_lower == False and ch.islower(): #test if current character is lowercase
            has_lower = True #set bool to True if condition is encountered
            
        if has_upper == False and ch.isupper(): #test if current character is uppercase
            has_upper = True #set bool to True if condition is encountered
    
        #test if all boolean values are true, indicating no further testing is required
        if is_alnum == True and is_alpha == True and has_digits == True and has_lower == True and has_upper == True:
            break #if no further testing is required, break from loop and print results
    
    print(f"{is_alnum}\n{is_alpha}\n{has_digits}\n{has_lower}\n{has_upper}") #print boolean values in order line separated