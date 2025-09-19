list = [
    {"name": "Bob",  "phone": "0632345678", "age": "20", "group": "1"},
    {"name": "Emma", "phone": "0974261525", "age": "21", "group": "2"},
    {"name": "Jon",  "phone": "0501569566", "age": "22", "group": "3"},
    {"name": "Zak",  "phone": "0738484849", "age": "19", "group": "4"}
]

def printAllList():
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + \
                      ", Phone is " + elem["phone"] + \
                      ", Age is " + elem["age"] + \
                      ", Group is " + elem["group"]
        print(strForPrint)
    return

def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    age = input("Please enter student age: ")
    group = input("Please enter student group: ")

    newItem = {"name": name, "phone": phone, "age": age, "group": group}

    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Delete position " + str(deletePosition))
        del list[deletePosition]
    return

def updateElement():
    name = input("Please enter name to be updated: ")
    updatePosition = -1
    for i, item in enumerate(list):
        if name == item["name"]:
            updatePosition = i
            break

    if updatePosition == -1:
        print("Element was not found")
        return

    print("Current data:", list[updatePosition])

    newName = input("Enter new name (or press Enter to keep '" + list[updatePosition]["name"] + "'): ") or list[updatePosition]["name"]
    newPhone = input("Enter new phone (or press Enter to keep '" + list[updatePosition]["phone"] + "'): ") or list[updatePosition]["phone"]
    newAge = input("Enter new age (or press Enter to keep '" + list[updatePosition]["age"] + "'): ") or list[updatePosition]["age"]
    newGroup = input("Enter new group (or press Enter to keep '" + list[updatePosition]["group"] + "'): ") or list[updatePosition]["group"]

    updatedItem = {"name": newName, "phone": newPhone, "age": newAge, "group": newGroup}

    del list[updatePosition]

    insertPosition = 0
    for item in list:
        if newName > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, updatedItem)

    print("Element has been updated")
    return

def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
                printAllList()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong choice")

main()