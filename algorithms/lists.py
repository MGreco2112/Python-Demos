if __name__ == '__main__':
    array = []
    N = int(input())
    
    for query in range(N):
        print(query)
        queryString = input()
        
        firstCharacter = queryString[0]
        
        if (firstCharacter == "i"):
            index = int(queryString[7])
            
            if (len(array) >= index):
                # TODO fix the substring call so errors are not thrown
                array.append(int(queryString[9:len(queryString)]))
            else:
                array[index] = int(queryString[9:len(queryString)])
            
        elif (firstCharacter == "p"):
            if (queryString[1] == "r"):
                print(array)
            else:
                array.pop()
            
        elif (firstCharacter == "r"):
            if (queryString[2] == "m"):
                array.remove(int(queryString[7:len(queryString)]))
            else:
                array.reverse()
                
        elif (firstCharacter == "a"):
            array.append(int(queryString[7:len(queryString)]))
            
        elif (firstCharacter == "s"):
            array.sort()
            