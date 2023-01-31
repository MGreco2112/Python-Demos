if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    #convert map to list
    listArr = list(arr)

    #sort list in ascending order
    listArr.sort()

    #locate highest score
    highestScore = listArr[len(listArr) - 1]

    #set current score
    score = 0

    #iterate through scores
    for x in listArr:
        #locate scores less than highest score
        if (x != highestScore):
            #store individual scores not highest into score
            score = x

    #print score
    print(score)
