stamp_set = set([]) # initialize empty set in stamp_set var

max_stamps = int(input()) #parse next line input as int to use in loop conditional

for stamp in range(max_stamps): #define for loop based upon input for range function
    
    stamp_set.add(input()) #add next line string input to set, repeat for range
    

    
print(len(stamp_set)) #output length of set, which is the number of distinct elements of the given dataset