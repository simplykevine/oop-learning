import math
i=int(input("enter number of students u wanna record: "))
students=[]
for n in range (i):
    student_name=input("enter name of student:")
    students.append(student_name)
for students in students:
    print(students)