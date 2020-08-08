def gradingStudents(grades):
    result=[]
    for i in grades:
        if i>37:
            if i%5==3:
                i=i+2
            elif i%5==4:
                i=i+1
        result.append(i)
    return result
if __name__ == '__main__':
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    result = gradingStudents(grades)
    for j in result:
        print(j)
