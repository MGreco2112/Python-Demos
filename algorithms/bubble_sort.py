#basic bubble sort array function

def bubble_sort(arr): #define bubble sort function that takes one argument

    swappedElements = True #initilize swappedElements boolean value to true, for use with the while loop

    while swappedElements: #define while loop referencing swappedElements for a condition
        swappedThisCycle = False #initialize swappedThisCycle boolean to False to monitor the progress of each iteration through the list
        for element in range(len(arr) - 1): #define for loop through range of the length of the array minus 1, to allow for looking at the coming index
            if arr[element] > arr[element + 1]: #if current element is greater than next element
                temp = arr[element] #initialize temp var to current element
                arr[element] = arr[element + 1] #change element at index of current element to next element
                arr[element + 1] = temp #change element at index of next element to stored temp variable
                swappedThisCycle = True #set swappedThisCycle to true, indicating that a change was made during this iteration
        
        if not swappedThisCycle: #if no change was made this cycle
            swappedElements = False #change conditional var in while loop to false, breaking loop
            
    
    return arr #return modified array

test = [5, 4, 3, 2, 1] #initialize test var to array not in numericl order (lowest to greatest)

print(bubble_sort(test)) #print the result of bubble sort on test

print(test) #print current value of test after bubble sort algorithm has run. This shows that this is a "destructive" algorithm
#the modifications done to the input data reflect the original data, not just the return value. I will find a way to perform these operations
#without destorying the original data set.