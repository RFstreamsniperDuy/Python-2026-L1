#Next version using pickle to store data:
import math
import pickle
import labwork1b_functions      
# for student

# This is for creating existed dfata for the student_information - cuz im lazy
# Class = [
#     (101, "Duy", "15/03/2004"),
#     (102, "Mai", "22/07/2004"),
#     (103, "RF", "10/11/2003"),
#     (104, "Alex", "05/01/2004"),
#     (105, "Sarah", "18/09/2004"),
#     (106, "John", "30/04/2003"),
#     (107, "Emma", "12/12/2004"),
#     (108, "Liam", "25/06/2004"),
#     (109, "Sophia", "08/02/2004"),
#     (110, "Lucas", "19/10/2003"),
# ]
# with open("Student_info.txt","wb") as new_student_input:
#         pickle.dump(Class,new_student_input)

#load the student_info.txt to a list 
# -> compare if the new input based on studentID as the system
# -> load new information on the txt file
with open("Student_info.txt","rb") as student_existed_info:
        existed_class = pickle.load(student_existed_info) # This will load all the data existed form the txt file

print("Current class:")
for i in existed_class:
        print(f"{i[0]}, {i[1]}, {i[2]}") # Print current student list

number_of_students = int(input("number of new student : "))
if number_of_students != 0:
        for i in range(number_of_students):
                studentID,student_name,student_DoB = labwork1b_functions.Newstudent(number_of_students)

        if labwork1b_functions.check_student_existed(studentID,existed_class):
                print("This ID has been used")
        else:
                print("New student input confirmed")
                existed_class.append((studentID,student_name,student_DoB))
                        
        with open("Student_info.txt","wb") as new_student_input:
                pickle.dump(existed_class,new_student_input) # overwrite old information with new student
else:
        print("Welp no new student i guess\n") # no new input no need to overwrite
# for courses

# courses = [
#     ["C101", "math"],
#     ["C102", "eng"],
#     ["C103", "science"],
#     ["C104", "history"],
#     ["C105", "art"],
# ]
# with open("Course_info.txt","wb") as new_course_input:
#         pickle.dump(courses,new_course_input)
with open("Course_info.txt","rb") as courses_existed_info:
       existed_courses = pickle.load(courses_existed_info)
print("Current existed courses:")
for i in existed_courses:
       print(f"{i[0]}, {i[1]}")

number_of_courses = int(input("Input number of new course: "))
if number_of_courses != 0:
        for i in range(number_of_courses):
                CourseID,Course_name = labwork1b_functions.NewCourse(number_of_courses)

        if labwork1b_functions.check_course_existed(CourseID,existed_courses):
                print("This ID has been used")
        else:
                print("New course input confirmed")
                existed_courses.append((CourseID,Course_name))
                        
        with open("Course_info.txt","wb") as new_course_input:
                pickle.dump(existed_courses,new_course_input) # overwrite old information with new student
else:
        print("Zero new class\n") # no new input then no need to overwrite again bruv

mark_section = {} # create for holding courses with each courses has values of student ID in them
for i in existed_courses: # begin creating list for courses
        mark_section[i[1]] = {} 
print(mark_section)
# input marks for student - every student join all the existed courses scenario 
while True:
        course_callout_marker = str(input("Input the course that you want to marking (0 if quit): "))
        if course_callout_marker == "0" :
                break
        else:
                for i in existed_class:
                      score_input = int(input(f"Input score of student {i[1]}-{i[0]}: "))
                      rounded_mark = math.floor(score_input*10)/10 # round down the score to 1-digit decimal for mark 
                      mark_section[course_callout_marker][i[0]] = rounded_mark
#asking score of student
for i in existed_class:
        print(f"{i[0]}-{i[1]}")
while True:
        callout_student_mark = int(input("Input the student ID to know the score (or press 0 to quit): "))
        if callout_student_mark != 0:
                for i in existed_class: 
                        if i[0] == callout_student_mark:
                                print(f"Name: {i[1]}, studentID: {i[0]}, Date of birth: {i[2]}")
                                break
                for i in mark_section:
                        score = mark_section[i].get(callout_student_mark,"No score")
                        print(f"{i}: {score}")
        else:
                print("All system offline")
                break