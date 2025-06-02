class Student:
    def __init__(self,name,courses):
        self.name = name
        self.courses = []

    def add(self,course,grade):
        self.courses.append(course,grade)
        course.add(self.courses, grade)

    def avg(self):
        if self.courses:
            return sum((self.courses.values()) / len(self.courses))
        return 0

class Course:
    def __init__(self,name,teacher,students):
        self.name = name
        self.teacher = teacher
        self.students = []

    def add(self,student,grade):
        self.students.append(student,grade)
        student.add(self.name,grade)

    def avg(self):
        if self.students:
            return sum(self.students.values()) / len(self.students)
        return 0





