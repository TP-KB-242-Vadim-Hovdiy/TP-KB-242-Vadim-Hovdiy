import unittest
import tempfile
import os
from lab2 import addNewElement, deleteElement, updateElement, save_to_csv, load_from_csv

class TestStudentCRUD(unittest.TestCase):

    def test_add_sorted(self):
        students = [
            {"name": "Bob", "phone": "0975858585", "age": "20", "group": "1"},
            {"name": "Dima", "phone": "1254572565", "age": "21", "group": "3"}
        ]

        inputs = iter(["Charlie", "042416825", "22", "5"])
        original_input = __builtins__.input
        __builtins__.input = lambda _: next(inputs)

        addNewElement(students)

        __builtins__.input = original_input

        self.assertEqual(len(students), 3)
        self.assertEqual(students[1]["name"], "Charlie")

    def test_delete(self):
        students = [
            {"name": "Alex", "phone": "01252525", "age": "19", "group": "6"},
            {"name": "Bob", "phone": "01245668", "age": "20", "group": "2"},
        ]

        inputs = iter(["Bob"])
        original_input = __builtins__.input
        __builtins__.input = lambda _: next(inputs)

        deleteElement(students)

        __builtins__.input = original_input

        self.assertEqual(len(students), 1)
        self.assertEqual(students[0]["name"], "Alex")

    def test_update(self):
        students = [
            {"name": "Alex", "phone": "111", "age": "19", "group": "5"},
            {"name": "Bob", "phone": "222", "age": "20", "group": "4"},
        ]

        inputs = iter([
            "Alex",
            "Charlie",
            "",
            "25",
            ""
        ])

        original_input = __builtins__.input
        __builtins__.input = lambda _: next(inputs)

        updateElement(students)

        __builtins__.input = original_input

        self.assertEqual(students[1]["name"], "Charlie")
        self.assertEqual(students[1]["age"], "25")

    def test_load_and_save_csv(self):
        temp = tempfile.NamedTemporaryFile(delete=False, mode="w", newline="")
        temp.write("name,phone,age,group\n")
        temp.write("Bob,115525596,20,1\n")
        temp.close()

        students = load_from_csv(temp.name)

        self.assertEqual(students[0]["name"], "Bob")

        save_to_csv(temp.name, students)

        students2 = load_from_csv(temp.name)
        self.assertEqual(students2[0]["phone"], "115525596")

        os.remove(temp.name)

if __name__ == "__main__":
    unittest.main()
