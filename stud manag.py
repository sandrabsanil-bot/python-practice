students = []


def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = float(input("Enter marks: "))

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    students.append(student)

    print("Student added successfully!\n")


def view_students():

    if len(students) == 0:
        print("No students found\n")

    else:
        print("\nStudent Records:")

        for student in students:
            print("----------------------")
            print("Name :", student["name"])
            print("Roll :", student["roll"])
            print("Marks:", student["marks"])

        print()


def search_student():

    roll = input("Enter roll number to search: ")

    found = False

    for student in students:

        if student["roll"] == roll:

            print("\nStudent Found")
            print("----------------------")
            print("Name :", student["name"])
            print("Roll :", student["roll"])
            print("Marks:", student["marks"])
            print()

            found = True
            break

    if found == False:
        print("Student not found\n")


def delete_student():

    roll = input("Enter roll number to delete: ")

    found = False

    for student in students:

        if student["roll"] == roll:

            students.remove(student)

            print("Student deleted successfully!\n")

            found = True
            break

    if found == False:
        print("Student not found\n")


while True:

    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Program exited")
        break

    else:
        print("Invalid choice\n")