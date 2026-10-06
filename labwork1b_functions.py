def Newstudent(number_of_students):       
        studentID = int(input("ID of this student: "))
        studentname= str(input("name of this student: "))
        studentDoB= str(input("Date of birth of this student: "))
        print("")
        return studentID,studentname,studentDoB

def NewCourse(number_of_course):
        CourseID = str(input("ID of this course: "))
        CourseName = str(input("Name of this course: "))
        Course_credit = int(input("Credit of this course: "))
        print("")
        return CourseID, CourseName, Course_credit

def check_student_existed(studentID,existed_class):
        for i in existed_class:
                if studentID == i[0]:
                        return True
        return False

def check_course_existed(CourseID,existed_courses):
        for i in existed_courses:
                if CourseID == i[0]:
                        return True
        return False

# def GPA_calculator(existed_class,existed_courses,mark_section,studentID):
# # class : ((studentID,Studentname,DOB),...)
# # Course: ((CourseID,Coursename,credits),...)
# # mark_section: {coursesname={studentid = mark,studentid = mark,...}}
# # based on input studentID

