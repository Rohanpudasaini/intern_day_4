import csv
from check_db import DatabaseHandler

class Student:
    def __init__(self, first_name, last_name, roll_number, paid, enrolled=None, total_cost=0, db_handler= DatabaseHandler("/home/r0h8n/Desktop/Vanilla/Day4.1/DB")):
        self.db_handler = db_handler
        self.first_name = first_name
        self.last_name = last_name
        self.roll_number = roll_number
        self.enrolled = enrolled if enrolled is not None else []
        self.paid = paid
        self.total_cost = total_cost

        self.student_data = self.db_handler.get_student()
        if self.roll_number not in self.student_data:
            self.student_data[self.roll_number] = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "Total_cost": self.total_cost,
                "Enrolled_list": self.enrolled,
                "Paid": self.paid
            }
            self.db_handler.write_student(self.student_data)

    def make_payment(self, pay):
        self.start_db_handeling(self)
        self.student_data = self.db_handler.get_student()
        self.student_data[self.roll_number]["Paid"] = str(float(self.student_data[self.roll_number]["Paid"]) + pay)
        self.db_handler.write_student(self.student_data)

    def update_total_price(self, id):
        self.start_db_handeling(self)
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
        self.start_db_handeling(self)
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
        
    
    # @classmethod
    # def FromStudentObject(cls, student:dict):
        # return (cls(student))



