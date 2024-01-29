# import csv
from check_db import DatabaseHandler
from display_functions import print_colored_message, Colors
import os

class Student:
    def __init__(self, first_name, last_name, roll_number, paid, enrolled=None, total_cost=0, db_handler= DatabaseHandler("/home/r0h8n/Desktop/Vanilla/Day4.1/DB")):
        self.db_handler = db_handler
        self.first_name = first_name
        self.last_name = last_name
        self.roll_number = roll_number
        self.enrolled = enrolled if enrolled is not None else []
        self.paid = paid
        self.total_cost = total_cost
        self.roll_number = int(self.roll_number)

        self.student_data = self.db_handler.get_student()
        # print(self.student_data)
        if self.roll_number not in self.student_data:
            self.student_data[self.roll_number] = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "Total_cost": self.total_cost,
                "Enrolled_list": self.enrolled,
                "Paid": self.paid
            }
        else:
            self.student_data[self.roll_number] = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "Total_cost": self.total_cost,
                "Enrolled_list": self.student_data[self.roll_number]["Enrolled_list"],
                "Paid": self.paid
            }
        # print(self.student_data)
        # input("Testing")
        self.db_handler.write_student(self.student_data)

    def make_payment(self, pay):
        # self.start_db_handeling(self)
        self.student_data = self.db_handler.get_student()
        self.student_data[self.roll_number]["Paid"] = str(float(self.student_data[self.roll_number]["Paid"]) + pay)
        self.db_handler.write_student(self.student_data)

    def update_total_price(self, id):
        # self.start_db_handeling(self)
        self.student_data = self.db_handler.get_student()
        _, all_course_list = self.db_handler.get_course()
        total_cost = 0
        student = self.db_handler.get_student()
        for course in student[id]["Enrolled_list"]:
            if course != "":
                total_cost += int(all_course_list[course])
        self.student_data[id]["Total_cost"] = str(total_cost)
        self.db_handler.write_student(self.student_data)

    def remaining_payment(self, id):
        # self.start_db_handeling(self)
        self.student_data = DatabaseHandler.get_student(DatabaseHandler)
        student = self.student_data.get(id, "Can't find the id in our Database")
        if isinstance(student, str):
            return student
        remaining = float(student["Total_cost"]) - float(student["Paid"])
        return remaining
    # def remaining_payment(self, id) ->float:
    #     self.student = self.db_handler.get_student()
    #     self.student = self.student.get(id, "Can't find the id in our Database")
    #     remaning = float(self.student["Total_cost"])- float(self.student["Paid"])
    #     return remaning

    def start_db_handeling(self):
        self.db_handler = DatabaseHandler()
        
    
    @staticmethod
    def get_student(db_handler):
        return db_handler.get_student()
    
    @staticmethod
    def write_student(db_handler, student):
        return db_handler.write_student(student)

class Academy:

    def start_db_handeling(self):
        self.db_handler = DatabaseHandler()
    @staticmethod  
    def add_academy(all_academy,db_handler):
        # all_academy, _ =  db_handler.get_course()
        academy_name = input("Enter Name of Academy: ")
        course_detail = input("Enter Academy details like (Coursename:price,coursename2:price) :")
        courses = course_detail.split(",")
        for course in courses:
            courses_name, course_price = course.split(":")
            if academy_name not in all_academy:
                all_academy[academy_name] = {courses_name:course_price}
            else:
                all_academy[academy_name].update({courses_name:course_price})
        db_handler.write_courses(all_academy)
        

    @staticmethod
    def remove_academy(all_academy,db_handler):
        remove = input("Enter Academy Name: ")
        if remove in all_academy:
            all_academy.pop(remove)
            db_handler.write_courses(all_academy)
        else:
            print_colored_message(f"Cant find the Academy named {remove}",Colors.RED)
        input("\n\nContinue...")
    
    @staticmethod
    def show_all_course(db_handler):
        os.system("clear")
        _, all_course_list = db_handler.get_course()
        print('''Course Name \t\t\t\t\t\t\t Course Price''')
        print("_"*100)
        for key, value in all_course_list.items():
            key = key.strip()
            if len(key) < 50:
                key += " " * (50-len(key))
            print_colored_message(f"{key} \t:\t {value.strip()}", Colors.YELLOW)
        input("\n\nContinue...")

    @staticmethod
    def get_course(db_handler):
        return db_handler.get_course()

