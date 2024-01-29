# Create a cli application where student can enroll in any academy.
# Student can opt out from that academy, student should be able to pay their fee in two installments, once at the start of enrollment, second on the next session start.
# In next session of that particular student, show prompt to pay the remaining due, if not paid.
# Student can enroll in any academy. Show the enrolled academy at the start of every new session. 
# Use OOP approach. Use interactive user interface to interact in cli application.

# Use csv files to read and write student's data.
import check_db
import csv
all_course, course_list = check_db.get_course()
class Student:
    def __init__(self, fname,lname, roll_no:str , paid:float, enrolled:list=[],total_cost = 0) -> None:
        self.fname = fname
        self.lname = lname
        self.roll_no = roll_no
        self.enrolled = enrolled
        self.paid = paid
        self.total_cost = total_cost
        self.student = check_db.get_student()
        # print(self.student)
        if self.roll_no not in self.student:
            self.student[self.roll_no] = {"fname":self.fname,"lname":self.lname,"Total_cost":self.total_cost,"Enrolled_list":self.enrolled,"Paid":self.paid}
        # student = student.update(check_db.create_student(fname, lname,roll_no,paid,enrolled))
        self.write_student(self.student)

    def create_student(fname, lname,roll_no,paid,enrolled_list = [], total_cost = 0):
        student = {}
        # enrolled = ','.join(enrolled_list)  # Convert list back to comma-separated string
        student[roll_no] = {"fname":fname, "lname":lname, "Total_cost":total_cost, "Enrolled_list":enrolled_list, "Paid":paid }
        # print(row)
        # rows.append(row)
        return student
        
     
    def make_payment(self, pay):
        self.student = check_db.get_student()
        self.student[self.roll_no]["Paid"] = str(float(self.student["Paid"]) + pay)
        check_db.write_student(self.student)

    def write_student(self, student:dict):
        with open("Student.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow(["first_name", "last_name","roll_num", "enrolled_course", "total_course_cost", "total_paid"])
            writer.writerows(check_db.make_row_student(student))

    def update_total_price(self, student):
        _, all_course_list = check_db.get_course()
        for roll, values in student.items():
            total_cost = 0
            for course in values["Enrolled_list"]:
                # print(all_course_list[course])
                if course != " ":
                    total_cost += int(all_course_list[course])
            student[roll]["Total_cost"] = str(total_cost)
        Student.write_student(Student,student)
    

    def remaning_payment(self, id) ->float:
        self.student = check_db.get_student()
        self.student = self.student.get(id, "Can't find the id in our Database")
        remaning = float(self.student["Total_cost"])- float(self.student["Paid"])
        return remaning
    
    def join_academy(self, academy):
        ...

    def leave_academy(self,  academy):
        ...

class Academy:
    def __init__(self,name:str,course_details:dict) -> None:
        self.name = name
        self.course_details = course_details
    
    def move_session(self):
        ...