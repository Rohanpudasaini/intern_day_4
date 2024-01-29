import os
from check_db import DatabaseHandler
from cli_app_class import Student

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'

def print_colored_message(message, color):
    print(color + message + Colors.RESET)

def main_menu():
    os.system('clear')
    print("\n\n\n\n")
    print_colored_message("\t\t\t\t\t\t1. Student", Colors.GREEN)
    print_colored_message("\t\t\t\t\t\t2. University", Colors.BLUE)
    print_colored_message("\t\t\t\t\t\t3. Cources", Colors.MAGENTA)
    print_colored_message("\t\t\t\t\t\t4. Exit", Colors.RED)
    print("\n\n\n\n")
    choice = input("\t\t\t\t\tEnter your choice: ")
    return choice

def welcome_screen():
    os.system("clear")
    print_colored_message("\n\n\t\t\t\t\t\tWelcome to the Educational App!\n\n\n\n", Colors.CYAN)
    print_colored_message('''
                                                                                                                        
    _/_/_/_/        _/                                  _/      _/                          _/    _/            _/       
   _/          _/_/_/  _/    _/    _/_/_/    _/_/_/  _/_/_/_/        _/_/    _/_/_/        _/    _/  _/    _/  _/_/_/    
  _/_/_/    _/    _/  _/    _/  _/        _/    _/    _/      _/  _/    _/  _/    _/      _/_/_/_/  _/    _/  _/    _/   
 _/        _/    _/  _/    _/  _/        _/    _/    _/      _/  _/    _/  _/    _/      _/    _/  _/    _/  _/    _/    
_/_/_/_/    _/_/_/    _/_/_/    _/_/_/    _/_/_/      _/_/  _/    _/_/    _/    _/      _/    _/    _/_/_/  _/_/_/       
                                                                                                                         
                                                                                                                                                                                                                                                                                                                                              
''', color=Colors.GREEN)
    input("\t\t\t\tPress any key to continue...")

def show_student(db_handler):
    os.system("clear")
    student = db_handler.get_student()
    print("Student Name |\t| Student Roll Number |\t| Enrolled List")
    for key, values in student.items():
        name = f"{values['first_name']} {values['last_name']}"
        count = len(name)
        if count < 15:
            name += " "*(15-count)
        if "" in values['Enrolled_list']:
            values['Enrolled_list'].remove('')

        print_colored_message(f"{name} |\t| {key} |\t\t| {values['Enrolled_list']}",Colors.YELLOW)
    choice = student_menu()
    match choice:
        case "1":
            last_roll_number = list(student.keys())[-1]
            firstname, lastname = input("Enter Students full name i.e name and surname only: ").split(" ")
            rollno = input(f"Enter unique rollnumber,(currentlast rollnumber is {last_roll_number}): ")
            current_paid = (input("Enter the current price paid: "))
            s1 = Student(firstname, lastname,rollno,float(current_paid))
            # db_handler.write

            # s1.write_student()

        case "2":
            roll_num_to_remove = input("Enter the roll number to remove: ")
            # print(student)
            student = db_handler.get_student()
            if roll_num_to_remove in student:
                student.pop(int(roll_num_to_remove))
                db_handler.write_student(student)
            else:
                print_colored_message(f"No student with roll number {roll_num_to_remove}", Colors.RED)
            # Student.db_handler.write_student(Student,student)
            input("Press anythin to continue...")
        case "3":
            student = db_handler.get_student()
            roll_num_to_fee = int(input("Enter the roll number to get remaning fee "))
            if roll_num_to_fee in student:
                print(Student.remaining_payment(Student,roll_num_to_fee))
            else:
                print_colored_message(f"No student with roll number {roll_num_to_fee}",Colors.RED)
            input("Press anythin to continue...")
        case "4":
            student = db_handler.get_student()
            roll_num_to_pay = int(input("Enter the roll number to get pay fee: "))
            if roll_num_to_pay in student:
                print(f"The student have {Student.remaining_payment(Student,roll_num_to_pay)} fee remaning, paid the fee now.")
                student = db_handler.get_student()
                student[int(roll_num_to_pay)]["Paid"] = float(student[int(roll_num_to_pay)]["Paid"]) + Student.remaining_payment(Student,roll_num_to_pay)
                db_handler.write_student(student)
            else:
                print_colored_message(f"No student with roll number {roll_num_to_pay}",Colors.RED)
            input("Enter anythin to continue....")
            
        case "5":
            roll_number_to_join = int(input("Enter the roll number to get Join a course: "))
            show_all_course(db_handler)
            _, all_course_list = db_handler.get_course()
            course_name_to_add = input("Enter the name of the course you want to add:  ").strip()
            if course_name_to_add in all_course_list:
                student = db_handler.get_student()
                # print(all_course_list)
                student[roll_number_to_join]["Enrolled_list"].append(course_name_to_add)
                db_handler.write_student(student)
                # s1 = Student()
                Student.update_total_price(Student, roll_number_to_join)
            else:
                print_colored_message("No Such Course Name", Colors.RED)
            input("\n Press any key to continue")


        case "6":
            roll_number_to_opt = int(input("Enter the roll number to get Opt from a course: "))
            # show_all_course()
            student = db_handler.get_student()
            course_name_to_remove = input("Enter the name of the course you want to remove:  ")
            if course_name_to_remove in student[roll_number_to_opt]["Enrolled_list"]:
                student[roll_number_to_opt]["Enrolled_list"].remove(course_name_to_remove)
                db_handler.write_student(student)
                Student.update_total_price(Student)
            else:
                print_colored_message("No Such Course Name", Colors.RED)
                input()
            

        case "7":
            print_colored_message("\n\t\tChanging Session",Colors.GREEN)
            student = db_handler.get_student()
            for key, values in student.items():
                remaning = Student.remaining_payment(Student, int(key))
                if  remaning > 0:
                    print_colored_message(f"\t\tThe Student {values['first_name']} have {remaning} fee, please check whith him/her once",Colors.RED)
                if  remaning < 0:
                    remaning = remaning * -1
                    print_colored_message(f"\t\tThe Student {values['first_name']} have {remaning} fee over charged, please check whith him/her once",Colors.GREEN)
            input("\n\nContinue ....")
        
        case "8":
            welcome_screen()
        case _:
            show_student()

    # Function body needs to be updated to interact with db_handler

def show_all_course(db_handler):
    # Function body needs to be updated to interact with db_handler
    os.system("clear")
    _, all_course_list = db_handler.get_course()
    print('''Course Name \t\t\t\t\t\t Course Price''')
    print("_"*80)
    for key, value in all_course_list.items():
        key = key.strip()
        if len(key) < 40:
            key += " " * (40-len(key))
        print_colored_message(f"{key} \t:\t {value}", Colors.YELLOW)
    input("Continue...")

def add_academy(all_academy, db_handler):
    # all_academy, _ =  db_handler.get_course()
    academy_name = input("Enter Name of Academy: ")
    course_detail = input("Enter Academy details like (Coursename:price,coursename2:price) :")
    cources = course_detail.split(",")
    for course in cources:
        cources_name, course_price = course.split(":")
        if academy_name not in all_academy:
            all_academy[academy_name] = {cources_name:course_price}
        else:
            all_academy[academy_name].update({cources_name:course_price})
    db_handler.write_courses(all_academy)

def remove_academy(all_academy, db_handler):
    remove = input("Enter Academy Name: ")
    if remove in all_academy:
        all_academy.pop(remove)
        db_handler.write_courses(all_academy)
    else:
        print_colored_message(f"Cant find the course name {remove}",Colors.RED)

def cources_menu():
    print_colored_message("\n\t\t\t1. Add Academy",Colors.GREEN)
    print_colored_message("\t\t\t2. Remove Academy",Colors.BLUE)
    print_colored_message("\t\t\t3. Exit",Colors.RED)
    print("\n\n\n\n")
    choice = input("\t\t\t\t\tEnter your choice: ")
    return choice

def show_university(db_handler):
    os.system("clear")
    all_academy, _ = db_handler.get_course()
    print('''Academy Name \t\t\t\t\t\t Cources and Price''')
    for key, values in all_academy.items():
        print("_"*80)
        print_colored_message(f"{key}", Colors.YELLOW)
        print("_"*80)
        for key2, values2 in values.items():
            print_colored_message(f"\t\t\t {key2.strip()}: {values2}",Colors.YELLOW) 
    choice = cources_menu()
    match choice:
        case "1":
            add_academy(all_academy,db_handler)
        case "2":
            remove_academy(all_academy, db_handler)
        case "3":
            welcome_screen()
        case _:
            show_university(db_handler)

def student_menu():
    print_colored_message("\n\t\t\t1. Add Student",Colors.GREEN)
    print_colored_message("\t\t\t2. Remove Student",Colors.RED)
    print_colored_message("\t\t\t3. Get Remaning Fee",Colors.BLUE)
    print_colored_message("\t\t\t4. Pay Remaning Fee",Colors.BLUE)
    print_colored_message("\t\t\t5. Join Cources",Colors.BLUE)
    print_colored_message("\t\t\t6. Opt Cources",Colors.BLUE)
    print_colored_message("\t\t\t7. Move session",Colors.BLUE)
    print_colored_message("\t\t\t8. Exit",Colors.RED)
    print("\n\n\n\n")
    choice = input("\t\t\t\t\tEnter your choice: ")
    return choice

def main():
    welcome_screen()
    db_handler = DatabaseHandler()
    while True:
        choice = main_menu()
        if choice == '1':
            show_student(db_handler)
        elif choice == '2':
            show_university(db_handler)
        elif choice == '3':
            show_all_course(db_handler)
        elif choice == '4':
            print("Exiting the app...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
