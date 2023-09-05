import random
import datetime
import re
name_pattern = r"^[A-Za-z]+$"  # to enter a correct student name , followed by this function


def is_valid_name(name):
    return bool(re.match(name_pattern, name))


now = datetime.datetime.now()  # to display date and time
time = now.strftime("%Y-%M-%d %H:%M%S")

print("          Welcome to Student Grader Advanced      ")
print(f"          You logged in at {time}                 ")
# this is a student grader platform that


class Student:
    """A class that defines the basic information for a student grader"""
    def __init__(self, name, familyname, grade, code):
        self.name = name
        self.familyname = familyname
        self.grade = grade
        self.code = random.randint(100000000, 999999999)
        self.fullname = name + " " + familyname

    def studentinfo(self):
        """Function will be used later in the options of the student grader, same for functions below"""
        return f"{self.fullname} ID: {self.code} has the following grade {self.grade}%"

    def studentcode(self):
        return f"{self.fullname} has the following unique student identifier {self.code}"


student_list = []  # to store the name for students to access them when needed
student_codes = {}  # a dic that takes the name of the student and appoints the followingcode
student_grades = {}

print("           Press change for more options      ")   # used to simpfly user input and to add students easier

while True:
    name = str(input("Please Enter student name : "))
    if name != "change" and is_valid_name(name): # to keep adding students until the user decides to change the option
        family_name = str(input(f"Please enter {name}'s family name: "))
        if is_valid_name(family_name):
            grade = float(input(f"Please Enter {name}'s grade: "))
            new_student = Student(name=name, familyname=family_name, grade=grade,
                                  code=random.randint(100000000, 999999999))
            print(new_student.studentinfo())
            student_list.append(new_student)
            student_codes.update({new_student.code: new_student.fullname})
            student_grades.update({new_student.fullname: new_student.grade})
    elif name == "change":  # Displays all the options
        print("Please choose an action:")
        print(" ")
        print("1- Display students' grade")
        print(" ")
        print("2- Display students' secret code")
        print(" ")
        print("3- Display Student info(Enter unique ID)")
        print(" ")
        print("4- Exit")
        print(" ")

        choice = int(input("Choose the option: "))

        if choice == 1:
            for student in student_list:
                print(student.studentinfo())

        elif choice == 2:
            for student in student_list:
                print(student.studentcode())

        elif choice == 3:
            student_code = int(input("Enter student secret code: "))
            student_name = student_codes.get(student_code)
            student_grade = student_grades[student_name]
            print(f"the student name is {student_name} and it has the following grade {student_grade}%")

        elif choice == 4:
            print("Thanks have a good day! ")
            break












