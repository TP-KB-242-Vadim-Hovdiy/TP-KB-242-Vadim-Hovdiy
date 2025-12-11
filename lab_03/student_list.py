from student import Student

class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        insert_pos = 0
        for s in self.students:
            if student.name > s.name:
                insert_pos += 1
            else:
                break
        self.students.insert(insert_pos, student)

    def find_by_name(self, name):
        for s in self.students:
            if s.name == name:
                return s
        return None

    def delete_student(self, name):
        for i, s in enumerate(self.students):
            if s.name == name:
                del self.students[i]
                return True
        return False

    def update_student(self, old_name, new_student: Student):
        if self.delete_student(old_name):
            self.add_student(new_student)
            return True
        return False

    def print_all(self):
        for s in self.students:
            print(
                f"Student name is {s.name}, Phone is {s.phone}, "
                f"Age is {s.age}, Group is {s.group}"
            )
