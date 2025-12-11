from sys import argv
from student import Student
from student_list import StudentList
from file_manager import FileManager


def main():
    if len(argv) < 2:
        print("Error: CSV file name must be provided!")
        return

    file_name = argv[1]

    group_list = StudentList()
    group_list.students = FileManager.load_from_csv(file_name)

    while True:
        choice = input("Select action [C create, U update, D delete, P print, X exit]: ")

        match choice:
            case "C" | "c":
                name = input("Enter student name: ")
                phone = input("Enter phone: ")
                age = input("Enter age: ")
                group = input("Enter group: ")

                st = Student(name, age, phone, group)
                group_list.add_student(st)

                group_list.print_all()

            case "U" | "u":
                old_name = input("Enter name to update: ")

                target = group_list.find_by_name(old_name)
                if not target:
                    print("Element not found.")
                    continue

                new_name = input(f"New name ({target.name}): ") or target.name
                new_phone = input(f"New phone ({target.phone}): ") or target.phone
                new_age = input(f"New age ({target.age}): ") or target.age
                new_group = input(f"New group ({target.group}): ") or target.group

                updated_student = Student(new_name, new_age, new_phone, new_group)

                group_list.update_student(old_name, updated_student)
                print("Element updated.")

                group_list.print_all()

            case "D" | "d":
                name = input("Enter name to delete: ")
                if group_list.delete_student(name):
                    print("Element deleted.")
                else:
                    print("Element not found.")

                group_list.print_all()

            case "P" | "p":
                group_list.print_all()

            case "X" | "x":
                print("Saving and exiting...")
                FileManager.save_to_csv(file_name, group_list.students)
                break

            case _:
                print("Wrong choice")


if __name__ == "__main__":
    main()
