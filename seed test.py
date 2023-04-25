#random number seeding test

import random #import random module

random.seed(10) #set the seed to a manual value, not determined by the system time value

for _ in range(4): #iterate from 0 to 3
    print(random.randint(1, 100)) #print randint return value with inclusive range 1 to 100
    #these four results are generated every time, as the initial random is generated via the seed call
    
    #74
    #5 
    #55
    #62