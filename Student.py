import json


FILE_NAME = "students.json"


# Load data from JSON file
def load_data():

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []



# Save data into JSON file
def save_data(data):

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)



# CREATE
def add_student():

    students = load_data()

    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))


    student = {
        "name": name,
        "marks": marks
    }


    students.append(student)

    save_data(students)

    print("Student Added Successfully")



# READ
def view_students():

    students = load_data()


    if not students:
        print("No students available")
        return


    print("\nStudent Details")

    for student in students:
        print("----------------")
        print("Name:", student["name"])
        print("Marks:", student["marks"])



# SEARCH
def search_student():

    students = load_data()

    name = input("Enter name to search: ")


    for student in students:

        if student["name"].lower() == name.lower():

            print("\nStudent Found")
            print(student)
            return


    print("Student Not Found")



# UPDATE
def update_student():

    students = load_data()

    name = input("Enter student name: ")


    for student in students:

        if student["name"].lower() == name.lower():

            new_marks = int(input("Enter new marks: "))

            student["marks"] = new_marks

            save_data(students)

            print("Student Updated")

            return


    print("Student Not Found")



# DELETE
def delete_student():

    students = load_data()

    name = input("Enter student name: ")


    for student in students:

        if student["name"].lower() == name.lower():

            students.remove(student)

            save_data(students)

            print("Student Deleted")

            return


    print("Student Not Found")



# Average marks
def average_marks():

    students = load_data()


    if len(students)==0:

        print("No students")

        return


    total = 0


    for student in students:

        total += student["marks"]


    average = total / len(students)


    print("Average Marks:", average)




# Main Menu
while True:


    print("""
========= Student Management System =========

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Average Marks
7. Exit

============================================
""")


    choice = input("Enter choice: ")



    if choice == "1":
        add_student()


    elif choice == "2":
        view_students()


    elif choice == "3":
        search_student()


    elif choice == "4":
        update_student()


    elif choice == "5":
        delete_student()


    elif choice == "6":
        average_marks()


    elif choice == "7":

        print("Thank You")

        break


    else:

        print("Invalid Choice")