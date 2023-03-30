if __name__ == '__main__':
    s = input()
    
    is_alnum = False
    is_alpha = False
    has_digits = False
    has_lower = False
    has_upper = False
    
    
    for ch in s:
        if ch.isalnum():
            is_alnum = True
        
        if ch.isalpha():
            is_alpha = True
        
        if ch.isdigit():
            has_digits = True
            
        if ch.islower():
            has_lower = True
            
        if ch.isupper():
            has_upper = True
    
    print(f"{is_alnum}\n{is_alpha}\n{has_digits}\n{has_lower}\n{has_upper}")