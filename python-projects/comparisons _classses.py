class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __lt__(self, other):
        return self.grade < other.grade

    def __le__(self, other):
        return self.grade <= other.grade

    def __eq__(self, other):
        return self.grade == other.grade

    def __ne__(self, other):
        return self.grade != other.grade

    def __gt__(self, other):
        return self.grade > other.grade

    def __ge__(self, other):
        return self.grade >= other.grade

    def __str__(self):
        return f"Student(name={self.name}, grade={self.grade})"


student1 = Student("Alice", 85)
student2 = Student("Bob", 90)

print(student1 < student2)  # True
print(student1 > student2)  # False
print(student1 == student2)  # False
print(student1 != student2)  # True
