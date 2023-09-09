import random
import re
import tkinter as tk
from tkinter import messagebox

name_pattern = r"^[A-Za-z]+$"


def is_valid_name(name):
    return bool(re.match(name_pattern, name))


class Student:
    def __init__(self, name, familyname, grade):
        self.name = name
        self.familyname = familyname
        self.grade = grade
        self.code = random.randint(100000000, 999999999)
        self.fullname = name + " " + familyname

    def studentinfo(self):
        return f"{self.fullname} ID: {self.code} has the following grade {self.grade}%"

    def studentcode(self):
        return f"{self.fullname} has the following unique student identifier {self.code}"


student_list = []
student_codes = {}
student_grades = {}

def add_student():
    name = name_entry.get()
    family_name = family_name_entry.get()
    grade = grade_entry.get()

    if is_valid_name(name) and is_valid_name(family_name):
        try:
            grade = float(grade)
        except ValueError:
            messagebox.showerror("Invalid Grade", "Please enter a valid grade (a number).")
            return

        new_student = Student(name=name, familyname=family_name, grade=grade)
        student_list.append(new_student)
        student_codes.update({new_student.code: new_student.fullname})
        student_grades.update({new_student.fullname: new_student.grade})
        update_display(new_student.studentinfo())
        clear_entries()
    else:
        messagebox.showerror("Invalid Name", "Please enter valid names (letters only).")


def display_students_info():
    display_text.delete(1.0, tk.END)
    for student in student_list:
        display_text.insert(tk.END, student.studentinfo() + "\n")


def display_students_code():
    display_text.delete(1.0, tk.END)
    for student in student_list:
        display_text.insert(tk.END, student.studentcode() + "\n")


def display_student_info():
    student_code = int(student_code_entry.get())
    student_name = student_codes.get(student_code)
    if student_name:
        student_grade = student_grades[student_name]
        display_text.delete(1.0, tk.END)
        display_text.insert(tk.END, f"The student name is {student_name} and has the following grade {student_grade}%\n")
    else:
        messagebox.showerror("Student Not Found", "Student with the provided code not found.")


def update_display(message):
    display_text.insert(tk.END, message + "\n")


def clear_entries():
    name_entry.delete(0, tk.END)
    family_name_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)
    student_code_entry.delete(0, tk.END)


# Create the main window
root = tk.Tk()
root.title("Student Grader")

# Create and place GUI components
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

family_name_label = tk.Label(root, text="Family Name:")
family_name_label.pack()
family_name_entry = tk.Entry(root)
family_name_entry.pack()

grade_label = tk.Label(root, text="Grade:")
grade_label.pack()
grade_entry = tk.Entry(root)
grade_entry.pack()

add_button = tk.Button(root, text="Add Student", command=add_student)
add_button.pack()

display_students_button = tk.Button(root, text="Display Students' Grade", command=display_students_info)
display_students_button.pack()

display_code_button = tk.Button(root, text="Display Students' Code", command=display_students_code)
display_code_button.pack()

student_code_label = tk.Label(root, text="Enter Student Code:")
student_code_label.pack()
student_code_entry = tk.Entry(root)
student_code_entry.pack()

display_student_button = tk.Button(root, text="Display Student Info", command=display_student_info)
display_student_button.pack()

display_text = tk.Text(root, height=10, width=50)
display_text.pack()

quit_button = tk.Button(root, text="Quit", command=root.destroy)
quit_button.pack()

root.mainloop()
