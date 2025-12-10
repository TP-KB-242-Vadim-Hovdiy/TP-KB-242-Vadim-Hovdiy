class Student: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f" {self.name} , {self.age} років"
students = [
Student("Zak", 20),
Student("Anna", 22),
Student("John", 19),
Student("Maria", 21),
Student("Bob", 23),
Student("Vadim", 19) 
]

sorted_students = sorted(students, key=lambda s: s.age)
print("Відсортований список студентів за віком:")
for student in sorted_students:
    print(student)
 