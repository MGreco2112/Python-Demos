if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_marks = student_marks[query_name]
    
    marks = 0
    
    for x in query_marks:
        marks += x
        
    output = marks / len(query_marks)
    
    if (len(str(output)) < 5):
        print(str(output) + "0")
    else:
        print(round(output, 2))
    