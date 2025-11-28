import csv
from sys import argv


def load_from_csv(file):
    students = []
    with open(file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({
                "name": row["name"],
                "phone": row["phone"],
                "age": row["age"],
                "group": row["group"]
            })
    return students


def save_to_csv(file, students):
    with open(file, "w", newline='') as file:
        fieldnames = ["name", "phone", "age", "group"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for s in students:
            writer.writerow(s)


def printAllList(students):
    for elem in students:
        print(f"Student name is {elem['name']}, Phone is {elem['phone']}, "
              f"Age is {elem['age']}, Group is {elem['group']}")


def addNewElement(students):
    name = input("Enter student name: ")
    phone = input("Enter phone: ")
    age = input("Enter age: ")
    group = input("Enter group: ")

    newItem = {"name": name, "phone": phone, "age": age, "group": group}

    insert_pos = 0
    for item in students:
        if name > item["name"]:
            insert_pos += 1
        else:
            break

    students.insert(insert_pos, newItem)
    print("New element added.")


def deleteElement(students):
    name = input("Enter name to delete: ")
    pos = -1

    for i, item in enumerate(students):
        if item["name"] == name:
            pos = i
            break

    if pos == -1:
        print("Element not found.")
    else:
        del students[pos]
        print("Element deleted.")


def updateElement(students):
    name = input("Enter name to update: ")
    pos = -1

    for i, item in enumerate(students):
        if item["name"] == name:
            pos = i
            break

    if pos == -1:
        print("Element not found.")
        return

    item = students[pos]

    newName = input(f"New name ({item['name']}): ") or item["name"]
    newPhone = input(f"New phone ({item['phone']}): ") or item["phone"]
    newAge = input(f"New age ({item['age']}): ") or item["age"]
    newGroup = input(f"New group ({item['group']}): ") or item["group"]

    updated = {"name": newName, "phone": newPhone, "age": newAge, "group": newGroup}

    del students[pos]

    insert_pos = 0
    for s in students:
        if newName > s["name"]:
            insert_pos += 1
        else:
            break

    students.insert(insert_pos, updated)
    print("Element updated.")

def main():
    if len(argv) < 2:
        print("Error: CSV file name must be provided!")
        return

    file_name = argv[1]
    students = load_from_csv(file_name)

    while True:
        choice = input("Select action [C create, U update, D delete, P print, X exit]: ")

        match choice:
            case "C" | "c":
                addNewElement(students)
                printAllList(students)

            case "U" | "u":
                updateElement(students)
                printAllList(students)

            case "D" | "d":
                deleteElement(students)
                printAllList(students)

            case "P" | "p":
                printAllList(students)

            case "X" | "x":
                print("Saving and exiting...")
                save_to_csv(file_name, students)
                break

            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()