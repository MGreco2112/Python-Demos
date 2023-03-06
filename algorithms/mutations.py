def mutate_string(string, position, character):
    output = ""
    
    split_str = [letter for letter in string]
    
    split_str[position] = character
    
    return output.join(split_str)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)