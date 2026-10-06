#Next version using pickle to store data:
import math
import pickle
import labwork1b_functions      
# This system still works with an empty class so no worries

# for student
# This is for creating existed dfata for the student_information - cuz im lazy
# Class = [
#     (101, "Duy", "15/03/2004"),
#     (102, "Mai", "22/07/2004"),
#     (103, "RF", "10/11/2003"),
# ]
# with open("Student_info.txt","wb") as new_student_input:
#         pickle.dump(Class,new_student_input)

# load the student_info.txt to a list 
# -> compare if the new input based on studentID as the system
# -> load new information on the txt file
with open("Student_info.txt","rb") as student_existed_info:
        existed_class = pickle.load(student_existed_info) # This will load all the data existed form the txt file

print("")
print("Current class:")
for i in existed_class:
        print(f"{i[0]}, {i[1]}, {i[2]}") # Print current student list

number_of_students = int(input("number of new student : "))
if number_of_students != 0:
        for i in range(number_of_students):
                studentID,student_name,student_DoB = labwork1b_functions.Newstudent(number_of_students)
                while labwork1b_functions.check_student_existed(studentID,existed_class) == True:
                        print("This ID has been used\n")
                        studentID,student_name,student_DoB = labwork1b_functions.Newstudent(number_of_students)
                else:
                        print("New student input confirmed\n")
                        existed_class.append((studentID,student_name,student_DoB))
        with open("Student_info.txt","wb") as new_student_input:
                pickle.dump(existed_class,new_student_input) # overwrite old information with new student                
else:
        print("Welp no new student i guess\n") # no new input no need to overwrite


# for courses
# courses = [
#     ["C101", "math", 3],
#     ["C102", "eng", 4],
# ]
# with open("Course_info.txt","wb") as new_course_input:
#         pickle.dump(courses,new_course_input)
with open("Course_info.txt","rb") as courses_existed_info:
       existed_courses = pickle.load(courses_existed_info)
print("Current existed courses:")
for i in existed_courses:
       print(f"{i[0]}, {i[1]}, ECTS: {i[2]}")

number_of_courses = int(input("Input number of new course: "))
if number_of_courses != 0:
        for i in range(number_of_courses):
                CourseID,Course_name,Course_cre = labwork1b_functions.NewCourse(number_of_courses)
                while labwork1b_functions.check_course_existed(CourseID,existed_courses) == True:
                        print("This course ID has been used\n")
                        CourseID,Course_name,Course_cre = labwork1b_functions.NewCourse(number_of_courses)
                else:
                        print("New course input confirmed\n")       
                        existed_courses.append((CourseID,Course_name,Course_cre))  
        with open("Course_info.txt","wb") as new_course_input:
                pickle.dump(existed_courses,new_course_input) # overwrite old information with new student
else:
        print("Zero new class\n") # no new input then no need to overwrite again bruv


# These are for input of students score based on student ID for each courses
with open("Student_mark.txt","rb") as existed_mark:
       mark_section = pickle.load(existed_mark)
for i in existed_courses: # begin creating list for courses
        if i[1] not in mark_section:
                mark_section[i[1]] = {} 

for i,l in mark_section.items(): # Print the whole list to check 
        print(f"{i} = {l}")

# input marks for student - every student join all the existed courses scenario 
while True:
        course_callout_marker = str(input("Input the course that you want to marking (0 if quit): "))
        if course_callout_marker == "0" :
                break
        else:
                for i in existed_class:
                      score_input = float(input(f"Input score of student {i[1]}-{i[0]}: "))
                      rounded_mark = math.floor(score_input*10)/10 # round down the score to 1-digit decimal for mark 
                      mark_section[course_callout_marker][i[0]] = rounded_mark
with open("Student_mark.txt","wb") as new_student_mark:
        pickle.dump(mark_section,new_student_mark) # overwrite with new marking input


#calculate the GPA for all student (scenerio of all courses are attended by all students)


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
                print()
                print("All system offline\n")
                break