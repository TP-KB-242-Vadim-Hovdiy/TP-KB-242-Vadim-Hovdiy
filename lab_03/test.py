import unittest
import os
from student import Student
from student_list import StudentList
from file_manager import FileManager

TEST_CSV = "test_students.csv"

class TestStudent(unittest.TestCase):
    def test_student_creation(self):
        s = Student("Alice", 20, "12345", "A1")
        self.assertEqual(s.name, "Alice")
        self.assertEqual(s.age, 20)
        self.assertEqual(s.phone, "12345")
        self.assertEqual(s.group, "A1")


class TestStudentList(unittest.TestCase):
    def setUp(self):
        self.list = StudentList()
        self.s1 = Student("Bob", 21, "11111", "B1")
        self.s2 = Student("Alice", 20, "22222", "A1")
        self.s3 = Student("Charlie", 22, "33333", "C1")
        self.list.add_student(self.s1)
        self.list.add_student(self.s2)
        self.list.add_student(self.s3)

    def test_add_student_order(self):
        names = [s.name for s in self.list.students]
        self.assertEqual(names, ["Alice", "Bob", "Charlie"])

    def test_find_by_name(self):
        self.assertEqual(self.list.find_by_name("Alice"), self.s2)
        self.assertIsNone(self.list.find_by_name("NotExist"))

    def test_delete_student(self):
        result = self.list.delete_student("Bob")
        self.assertTrue(result)
        self.assertIsNone(self.list.find_by_name("Bob"))
        self.assertFalse(self.list.delete_student("Bob"))  

    def test_update_student(self):
        new_s = Student("Alice", 23, "99999", "A2")
        updated = self.list.update_student("Alice", new_s)
        self.assertTrue(updated)
        s = self.list.find_by_name("Alice")
        self.assertEqual(s.age, 23)
        self.assertEqual(s.phone, "99999")
        self.assertEqual(s.group, "A2")


class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.students = [
            Student("Alice", 20, "12345", "A1"),
            Student("Bob", 21, "11111", "B1")
        ]

    def tearDown(self):
        if os.path.exists(TEST_CSV):
            os.remove(TEST_CSV)

    def test_save_and_load_csv(self):
        FileManager.save_to_csv(TEST_CSV, self.students)
        loaded = FileManager.load_from_csv(TEST_CSV)
        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0].name, "Alice")
        self.assertEqual(loaded[1].phone, "11111")


if __name__ == "__main__":
    unittest.main()
