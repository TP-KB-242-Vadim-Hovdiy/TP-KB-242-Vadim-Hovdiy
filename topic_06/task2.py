students = [
    {"name": "Mark", "grade": 75},
    {"name": "Dan", "grade": 95},
    {"name": "John", "grade": 82},
    {"name": "Anna", "grade": 90},
    {"name": "Mary", "grade": 68},
    {"name": "Steve", "grade": 88}
]

print("Невідсортований список :")
for elem in students:
    print(f"Name = {elem['name']}  grade = {elem['grade']}")

print("\nСортування за ім'ям:")
sorted_students = sorted(students, key=lambda x: x["name"])
for elem in sorted_students:
    print(f"Name = {elem['name']}  grade = {elem['grade']}")
