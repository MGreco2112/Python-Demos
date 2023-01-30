def sortByScore(records):
    records.sort(key = lambda x: x[1])
    return records

def sortByName(records):
    records.sort(key = lambda x: x[0])
    return records

if __name__ == '__main__':
    records = []
    score = 0
    output = ""
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        records.append([name, score])
    
    sortByScore(records)
    
    lowestScore = records[0][1]
    
    for x in range(len(records)):
        if (records[x][1] != lowestScore):
            score = records[x][1]
            break
    
    sortByName(records)        
    
    for x in range(len(records)):
        if (score == records[x][1]):
            output += records[x][0] + "\n"
    
    print(output.strip())
