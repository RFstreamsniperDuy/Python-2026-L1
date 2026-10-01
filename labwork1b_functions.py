def Newstudent(number_of_students):       
        studentID = int(input("ID of this student: "))
        studentname= str(input("name of this student: "))
        studentDoB= str(input("Date of birth of this student: "))
        return studentID,studentname,studentDoB

def NewCourse(number_of_course):
        CourseID = int(input("ID of this course: "))
        CourseName = str(input("Name of this course: "))
        return CourseID, CourseName

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
