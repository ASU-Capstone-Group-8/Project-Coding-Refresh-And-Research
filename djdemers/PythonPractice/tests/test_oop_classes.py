# Test for OOP Classes
# tests/test_oop_classes.py
import unittest

from intermediate.oop_classes import Person, Student, Teacher, Classroom


class TestOOPClasses(unittest.TestCase):
    def test_person_greet(self):
        person = Person("David", 37)
        self.assertEqual(person.greet(), "Hello, my name is David and I am 37 years old.")

    def test_student_inheritance(self):
        student = Student("Aaron", 41, "S12345")
        self.assertEqual(student.greet(), "Hello, my name is Aaron and I am 41 years old.")
        self.assertEqual(student.study(), "Aaron is studying.")

    def test_teacher_teach(self):
        teacher = Teacher("Dr. M", 72, "Mathematics")
        self.assertEqual(teacher.teach(), "Dr. M is teaching Mathematics.")

    def test_classroom_activity(self):
        teacher = Teacher("Dr. J", 42, "English")
        student1 = Student("Ted", 20, "S12345")
        student2 = Student("Jessie", 22, "S12346")
        classroom = Classroom(teacher, [student1, student2])
        activities = classroom.classroom_activity()
        self.assertEqual(activities, [
            "Dr. J is teaching English.",
            "Ted is studying.",
            "Jessie is studying."
        ])

if __name__ == "__main__":
    unittest.main()