import check_db
import os
from cli_app_class import Student
# ANSI escape codes for colors
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

    print_colored_message("\t\t\t\t\t\t1. Student",Colors.GREEN)
    print_colored_message("\t\t\t\t\t\t2. University",Colors.BLUE)
    print_colored_message("\t\t\t\t\t\t3. Cources",Colors.MAGENTA)
    print_colored_message("\t\t\t\t\t\t4. Exit",Colors.RED)
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
def show_student():
    os.system("clear")
    student = (check_db.get_student())
    print("Student Name |\t| Student Roll Number |\t| Enrolled List")
    for key, values in student.items():
        name = f"{values['fname']} {values['lname']}"
        count = len(name)
        if count < 15:
            name += " "*(15-count)
        print_colored_message(f"{name} |\t| {key} |\t\t| {values['Enrolled_list']}",Colors.YELLOW)
    choice = student_menu()
    match choice:
        case "1":
            lst_roll_number = list(student.keys())[-1]
            firstname, lastname = input("Enter Students full name i.e name and surname only: ").split(" ")
            rollno = input(f"Enter unique rollnumber,(currentlast rollnumber is {lst_roll_number}): ")
            current_paid = (input("Enter the current price paid: "))
            s1 = Student(firstname, lastname,rollno,float(current_paid))
            # s1.write_student()

        case "2":
            roll_num_to_remove = input("Enter the roll number to remove: ")
            print(student)
            student.pop(int(roll_num_to_remove))
            Student.write_student(Student,student)

        case "3":
            roll_num_to_fee = int(input("Enter the roll number to get remaning fee: "))
            print(Student.remaning_payment(Student,roll_num_to_fee))
            input("Press anythin to continue...")
        case "4":
            roll_num_to_pay = int(input("Enter the roll number to get pay fee: "))
            print(f"The student have {Student.remaning_payment(Student,roll_num_to_pay)} fee remaning, paid the fee now.")
            student = check_db.get_student()
            student[int(roll_num_to_pay)]["Paid"] = float(student[int(roll_num_to_pay)]["Paid"]) + Student.remaning_payment(Student,roll_num_to_pay)
            Student.write_student(Student,student)
            input("Enter anythin to continue....")
            
        case "5":
            roll_no_to_join = int(input("Enter the roll number to get Join a course: "))
            show_all_course()

            course_name_to_add = input("Enter the name of the course you want to add:  ").strip()
            if  len(course_name_to_add) !=0:
                student = check_db.get_student()
                # print(all_course_list)
                student[roll_no_to_join]["Enrolled_list"].append(course_name_to_add)
                Student.write_student(Student,student)
                Student.update_total_price(Student, student)


        case "6":
            roll_no_to_opt = int(input("Enter the roll number to get Opt from a course: "))
            # show_all_course()
            student = check_db.get_student()
            course_name_to_remove = input("Enter the name of the course you want to remove:  ")
            student[roll_no_to_opt]["Enrolled_list"].remove(course_name_to_remove)
            Student.write_student(Student,student)
            Student.update_total_price(Student, student)

        case "7":
            welcome_screen()
        case _:
            show_student()

def show_all_course():
    os.system("clear")
    _, all_course_list = check_db.get_course()
    print('''Course Name \t\t\t\t\t\t Course Price''')
    print("_"*80)
    for key, value in all_course_list.items():
        key = key.strip()
        if len(key) < 40:
            key += " " * (40-len(key))
        print_colored_message(f"{key} \t:\t {value}", Colors.YELLOW)
    input("Continue...")
def add_academy(all_academy):
    academy_name = input("Enter Name of Academy: ")
    course_detail = input("Enter Academy details like (Coursename:price,coursename2:price) :")
    cources = course_detail.split(",")
    for course in cources:
        cources_name, course_price = course.split(":")
        if academy_name not in all_academy:
            all_academy[academy_name] = {cources_name:course_price}
        else:
            all_academy[academy_name].update({cources_name:course_price})
    check_db.write_courses(all_academy)
def remove_academy(all_academy:dict):
    remove = input("Enter Academy Name: ")
    all_academy.pop(remove)
    check_db.write_courses(all_academy)
def cources_menu():
    print_colored_message("\n\t\t\t1. Add Academy",Colors.GREEN)
    print_colored_message("\t\t\t2. Remove Academy",Colors.BLUE)
    print_colored_message("\t\t\t3. Exit",Colors.RED)
    print("\n\n\n\n")
    choice = input("\t\t\t\t\tEnter your choice: ")
    return choice
def show_university():
    os.system("clear")
    all_academy, _ = check_db.get_course()
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
            add_academy(all_academy)
        case "2":
            remove_academy(all_academy)
        case "3":
            welcome_screen()
        case _:
            show_university()
def student_menu():
    print_colored_message("\n\t\t\t1. Add Student",Colors.GREEN)
    print_colored_message("\t\t\t2. Remove Student",Colors.BLUE)
    print_colored_message("\t\t\t3. Get Remaning Fee",Colors.RED)
    print_colored_message("\t\t\t4. Pay Remaning Fee",Colors.BLUE)
    print_colored_message("\t\t\t5. Join Cources",Colors.BLUE)
    print_colored_message("\t\t\t6. Opt Cources",Colors.BLUE)
    print_colored_message("\t\t\t7. Exit",Colors.RED)
    print("\n\n\n\n")
    choice = input("\t\t\t\t\tEnter your choice: ")
    return choice



def main():
    welcome_screen()
    while True:
        choice = main_menu()
        if choice == '1':
            show_student()
        elif choice == '2':
            show_university()
        elif choice == '3':
            show_all_course()
            
        elif choice == '4':
            print("Exiting the app...")
            break
        else:
            print("Invalid choice. Please try again.")

main()


