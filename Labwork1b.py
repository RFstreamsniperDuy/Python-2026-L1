# for student
Class= []
number_of_students = int(input("Input number of students for this class: "))
def Newstudent(number_of_students):       
        studentID = int(input("ID of this student: "))
        studentname= str(input("name of this student: "))
        studentDoB= str(input("Date of birth of this student: "))
        return studentID,studentname,studentDoB
for i in range(number_of_students):
        Class.append(Newstudent(number_of_students))

# for courses
Courses = []
number_of_courses = int(input("Input number of courses existed: "))
def NewCourse(number_of_course):
        CourseID = int(input("ID of this course: "))
        CourseName = str(input("Name of this course: "))
        return CourseID, CourseName
for i in range(number_of_courses):
        Courses.append(NewCourse(number_of_courses))
print(Courses)

# select course -> Create dictionary based on course ID
# create loop to insert student score
# input each student mark

# courses = {course_name_mark:{id : ... ; id: ...}}
# class = [(id,name,dob),(id,name,dob),...]

mark_section = {}
for i in Courses: # begin creating list for courses
        mark_section[i[1]] = {} 
print(mark_section)
while True:
        course_callout_marker = str(input("Input the course that you want to marking (0 if quit): "))
        for i in Class:
                mark_section[course_callout_marker][i[0]] = int(input(f"Input score of student {i[1]}-{i[0]}: "))
        if course_callout_marker == 0 :
                break
print(mark_section)

# asking score of student

print(Class)
callout_student_mark = int(input("Input the student ID to know the score: "))

# we can use a function that called findind_student_ID to get the id of the student based on their input name 
# => based on return value of that ID -> callout on the list
for i in mark_section:
        print(f"{i}: {mark_section[i][callout_student_mark]}")
        
# What is the format of answer : student_name, course_A: score, course_B : score

#create input for student namem ID and Dob
# => create dictionary that include students list?
# format: class has 2 students {{ID1,name1,DoB1},{ID2,name2,DoB2}}

# for i in range(number_of_students):
#     studentID = int(input("ID of this student:"))
#     studentname= str(input("name of this student:"))
#     studentDoB= str(input("Date of birth of this student:"))
#     Class["num"] = i
#     students["ID"] = studentID
#     students["name"] = studentname
#     students["Dob"] = studentDoB
# print(students)