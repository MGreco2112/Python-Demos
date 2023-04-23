#basic bubble sort array function

def bubble_sort(arr):
    output = arr

    reset = False

    for pointer in range(len(output) - 1):

        print(pointer)
        if output[pointer] > output[pointer + 1]:
            temp = output[pointer]
            output[pointer] = output[pointer + 1]
            output[pointer + 1] = temp
            reset = True
        
        if reset:
            pointer = 0
            print(pointer)
            
    
    return output

test = [5, 4, 3, 2, 1]

print(bubble_sort(test))