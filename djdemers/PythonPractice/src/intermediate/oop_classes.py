# src/intermediate/oop_classes.py

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        return f"{self.name} is studying."

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        return f"{self.name} is teaching {self.subject}."

class Classroom:
    def __init__(self, teacher, students):
        self.teacher = teacher
        self.students = students

    def classroom_activity(self):
        activities = [self.teacher.teach()]
        for student in self.students:
            activities.append(student.study())
        return activities

if __name__ == "__main__":
    teacher = Teacher("Dr. Neil", 55, "Physics")
    student1 = Student("David", 37, "S12344")
    student2 = Student("Aaron", 41, "S12345")
    classroom = Classroom(teacher,[student1, student2])
    print(teacher.greet())
    print(student1.greet())
    print(student2.study())
    for activity in classroom.classroom_activity():
        print(activity)