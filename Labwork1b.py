import labwork1b_functions
# for student
Class= [] # create a class to hold all student personal information
number_of_students = int(input("Input number of students for this class: "))

for i in range(number_of_students):
        Class.append(labwork1b_functions.Newstudent(number_of_students))

# for courses
Courses = [] #create a list of courses to hold all course information
number_of_courses = int(input("Input number of courses existed: "))

for i in range(number_of_courses):
        Courses.append(labwork1b_functions.NewCourse(number_of_courses))
print(Courses)

mark_section = {} # create for holding courses with each courses has values of student ID in them
for i in Courses: # begin creating list for courses
        mark_section[i[1]] = {} 
print(mark_section)
# input marks for student - every student join all the existed courses scenario 
while True:
        course_callout_marker = str(input("Input the course that you want to marking (0 if quit): "))
        if course_callout_marker == "0" :
                break
        else:
                for i in Class:
                        mark_section[course_callout_marker][i[0]] = int(input(f"Input score of student {i[1]}-{i[0]}: "))

#asking score of student
for i in Class:
        print(f"{i[0]}-{i[1]}")
while True:
        callout_student_mark = int(input("Input the student ID to know the score (or press 0 to quit): "))
        if callout_student_mark != 0:
                for i in Class: 
                        if i[0] == callout_student_mark:
                                print(f"Name: {i[1]}, studentID: {i[0]}, Date of birth: {i[2]}")
                                break
                for i in mark_section:
                        score = mark_section[i].get(callout_student_mark,"No score")
                        print(f"{i}: {score}")
        else:
                print("All system offline")
                break

# FREE example: cuz im too lazy bruh im aint pressing the same input for 500 times (i did)
# mark_section = {"math": {24: 18,25: 15,26: 12},"eng": {24: 16,25: 19,26: 14},"physics": {24: 17,25: 14,26: 16}}
# Courses = [(101, "math"),(102, "eng"),(103, "physics")]
# Class = [(24, "Duy", "13/05/2004"),(25, "Mai", "22/09/2004"),(26, "Alex", "05/11/2003")]