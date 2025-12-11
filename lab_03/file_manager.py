import csv
from student import Student

class FileManager:

    @staticmethod
    def load_from_csv(filename):
        students = []
        try:
            with open(filename, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    students.append(
                        Student(
                            name=row["name"],
                            age=row["age"],
                            phone=row["phone"],
                            group=row["group"]
                        )
                    )
        except FileNotFoundError:
            pass

        return students

    @staticmethod
    def save_to_csv(filename, students):
        with open(filename, "w", newline='') as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["name", "phone", "age", "group"]
            )
            writer.writeheader()

            for s in students:
                writer.writerow({
                    "name": s.name,
                    "phone": s.phone,
                    "age": s.age,
                    "group": s.group
                })
