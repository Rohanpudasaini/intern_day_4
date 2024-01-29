import os
from check_db import DatabaseHandler
from cli_app_class import Student, Academy
from display_functions import *

def show_student_rows(db_handler):
    os.system("clear")
    student = Student.get_student(db_handler)
    print("Student Name |\t| Student Roll Number |\t| Enrolled List")
    for key, values in student.items():
        name = f"{values['first_name']} {values['last_name']}"
        count = len(name)
        if count < 15:
            name += " "*(15-count)
        if "" in values['Enrolled_list']:
            values['Enrolled_list'].remove('')
        print_colored_message(f"{name} |\t| {key} |\t\t| {values['Enrolled_list']}",Colors.YELLOW)
    choice = show_student_menu()
    match choice:
        case "1":
            last_roll_number = list(student.keys())[-1]
            full_name = input("Enter Students full name i.e name and surname only: ").split(" ",1)
            if len(full_name) ==2:
                firstname, lastname = full_name
            else:
                firstname = "".join(full_name)
                lastname = ""
            rollno = input(f"Enter unique rollnumber,(currentlast rollnumber is {last_roll_number}): ")
            current_paid = (input("Enter the current price paid: "))
            Student(firstname, lastname,rollno,float(current_paid))

        case "2":
            roll_num_to_remove = int(input("Enter the roll number to remove: "))
            student = Student.get_student(db_handler)
            if roll_num_to_remove in student:
                student.pop(int(roll_num_to_remove))
                Student.write_student(db_handler,student)
            else:
                print_colored_message(f"No student with roll number {roll_num_to_remove}", Colors.RED)
            input("\n\nPress anykey to continue...")

        case "3":
            student = Student.get_student(db_handler)
            roll_num_to_fee = int(input("Enter the roll number to get remaning fee "))
            if roll_num_to_fee in student:
                print(Student.remaining_payment(Student,roll_num_to_fee))
            else:
                print_colored_message(f"No student with roll number {roll_num_to_fee}",Colors.RED)
            input("\n\nPress anykey to continue...")

        case "4":
            student = Student.get_student(db_handler)
            roll_num_to_pay = int(input("Enter the roll number to get pay fee: "))
            if roll_num_to_pay in student:
                print(f"The student have {Student.remaining_payment(Student,roll_num_to_pay)} fee remaning, paid the fee now.")
                # student = Student.get_student()
                student[int(roll_num_to_pay)]["Paid"] = float(student[int(roll_num_to_pay)]["Paid"]) + Student.remaining_payment(Student,roll_num_to_pay)
                Student.write_student(db_handler,student)
            else:
                print_colored_message(f"No student with roll number {roll_num_to_pay}",Colors.RED)
            input("\n\nEnter anykey to continue....")
            
        case "5":
            roll_number_to_join = int(input("Enter the roll number to get Join a course: "))
            Academy.show_all_course(db_handler)
            _, all_course_list = Academy.get_course(db_handler)
            course_name_to_add = input("Enter the name of the course you want to add:  ").strip()
            if course_name_to_add in all_course_list:
                student = Student.get_student(db_handler)
                # print(all_course_list)
                if course_name_to_add not in student[roll_number_to_join]["Enrolled_list"]:
                    student[roll_number_to_join]["Enrolled_list"].append(course_name_to_add)
                    Student.write_student(db_handler,student)
                # s1 = Student()
                    Student.update_total_price(Student, roll_number_to_join)
                else:
                    print_colored_message(f"The User with roll number {roll_number_to_join} is already enrolled into {course_name_to_add} course")
            else:
                print_colored_message("No Such Course Name", Colors.RED)
            input("\n Press any key to continue")

        case "6":
            roll_number_to_opt = int(input("Enter the roll number to get Opt from a course: "))
            # show_all_course()
            student = Student.get_student(db_handler)
            course_name_to_remove = input("Enter the name of the course you want to remove:  ")
            if course_name_to_remove in student[roll_number_to_opt]["Enrolled_list"]:
                student[roll_number_to_opt]["Enrolled_list"].remove(course_name_to_remove)
                Student.write_student(db_handler,student)
                Student.update_total_price(Student)
            else:
                print_colored_message("No Such Course Name", Colors.RED)
                input()

        case "7":
            print_colored_message("\n\t\tChanging Session",Colors.GREEN)
            student = Student.get_student(db_handler)
            for key, values in student.items():
                remaning = Student.remaining_payment(Student, int(key))
                if  remaning > 0:
                    print_colored_message(f"\t\tThe Student {values['first_name']} have {remaning} fee, please check whith him/her once",Colors.RED)
                if  remaning < 0:
                    remaning = remaning * -1
                    print_colored_message(f"\t\tThe Student {values['first_name']} have {remaning} fee over charged, please check whith him/her once",Colors.GREEN)
            input("\n\nContinue ....")
        
        case "8":
            show_welcome_screen()
        case _:
            show_student_rows()

def show_university(db_handler):
    os.system("clear")
    all_academy, _ = Academy.get_course(db_handler)
    print('''Academy Name \t\t\t\t\t\t Courses and Price''')
    for key, values in all_academy.items():
        print("_"*80)
        print_colored_message(f"{key}", Colors.YELLOW)
        print("_"*80)
        for key2, values2 in values.items():
            print_colored_message(f"\t\t\t {key2.strip()}: {values2}",Colors.YELLOW) 
    choice = show_courses_menu()
    match choice:
        case "1":
            Academy.add_academy(all_academy,db_handler)
        case "2":
            Academy.remove_academy(all_academy, db_handler)
        case "3":
            show_welcome_screen()
        case _:
            show_university(db_handler)

def main():
    show_welcome_screen()
    db_handler = DatabaseHandler()
    Student.start_db_handeling(Student)
    Academy.start_db_handeling(Academy)
    while True:
        choice = show_main_menu()
        if choice == '1':
            show_student_rows(db_handler)
        elif choice == '2':
            show_university(db_handler)
        elif choice == '3':
            Academy.show_all_course(db_handler)
        elif choice == '4':
            print("Exiting the app...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
