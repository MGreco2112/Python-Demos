#basic bubble sort array function

def bubble_sort(arr):
    output = arr

    for _ in range(len(output) - 1):
        if output[_] > output[_ + 1]:
            temp = output[_]
            output[_] = output[_ + 1]
            output[_ + 1] = temp
            _ = 0
    
    return output

test = [5, 4, 3, 2, 1]

print(bubble_sort(test))