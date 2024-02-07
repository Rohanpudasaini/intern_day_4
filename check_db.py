from os import chdir, listdir
import csv
import json
chdir("./DB")


def get_course():
    academy_dict = {}
    all_academy = {}
    with open("Academy.csv","r") as file:
        reader = csv.reader(file)
        for i, rows in enumerate(reader):
            if i == 0:
                continue
            academy, courses = rows
            courses = courses.split(',')
            # print(courses)
            for course in courses:
                # print(course)
                course_name, course_price = course.split(":")
                course_name = course_name.strip()
                if academy not in academy_dict:
                    academy_dict[academy] = {course_name:course_price}
                else:
                    academy_dict[academy].update({course_name:course_price})
                all_academy[course_name] = course_price

            # academy_dict = academy_dict[academy] + make_dict(courses)
        
        # academy_dict_json = json.dumps(academy_dict, indent=4)
        return (academy_dict, all_academy)
    
def get_student():
    student = {}
    with open("Student.csv",'r') as file:
        reader = csv.reader(file)
        for i, rows in enumerate(reader):
            if i == 0:
                continue
            fname, lname, roll_no, enrolled, total_cost, paid = rows
            roll_no = int(roll_no)
            enrolled_list = enrolled.split(",")
            student[roll_no] = {"fname":fname.strip(), "lname":lname.strip(), "Total_cost":total_cost.strip(), "Enrolled_list":enrolled_list, "Paid":paid.strip() }
        # print(json.dumps(student, indent=4))
        return student
def create_student(fname, lname,roll_no,paid,enrolled_list = [], total_cost = 0):
    student = {}
    # enrolled = ','.join(enrolled_list)  # Convert list back to comma-separated string
    student[roll_no] = {"fname":fname, "lname":lname, "Total_cost":total_cost, "Enrolled_list":enrolled_list, "Paid":paid }
    # print(row)
    # rows.append(row)
    return student

def make_row_student(student):
    rows = []
    for roll_no, details in student.items():
        fname = details['fname']
        lname = details['lname']
        total_cost = details['Total_cost']
        paid = details['Paid']
        enrolled = ','.join(details['Enrolled_list'])  # Convert list back to comma-separated string
        row = [fname, lname, str(roll_no), enrolled, total_cost, paid]
        # if len(enrolled) !=0:
        #     
        
        # print(row)
        rows.append(row)
    return(rows)    

# def write_student(student:dict):
#     with open("Student.csv", "w") as file:
#         writer = csv.writer(file)
#         writer.writerow(["first_name", "last_name","roll_num", "enrolled_course", "total_course_cost", "total_paid"])
#         writer.writerows(make_row_student(student))
        # writer.writerows(rows)
def write_courses(academy_dict):
    with open("Academy.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(["Academy", "Courses"])
        for academy, courses in academy_dict.items():
            # Convert the courses dictionary to a string
            courses_str = ','.join([f"{course}:{price}" for course, price in courses.items()])
            writer.writerow([academy, courses_str])


# def update_student(student:dict ,**kwargs):



# write_student(get_student())

# x = map(lambda x: x[])

# academy_dict , all_academy = (get_course())

# print(academy_dict)
# # print("*"*20)
# print(all_academy)


# print(get_student())
# student = get_student()
# value = student.get(11,"Cant find in database")
# print(float(value["Total_cost"])- float(value["Paid"]))
