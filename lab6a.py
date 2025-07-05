#!/usr/bin/env python3
# Author ID: mebrahimi22

class Student:

    # creates a student and converts number to string
    def __init__(self, name, number):
        self.name = name
        self.number = str(number)  # this will convert thhe number to string just in case
        self.courses = {}

    # student info
    def displayStudent(self):
        return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + self.number

    # this will add the grade to the dictionary
    def addGrade(self, course, grade):
        self.courses[course] = grade

    # this will calculate gpa and will avoid ZeroDivisionError manually
    def displayGPA(self):
        total = 0.0
        count = 0

        for course in self.courses:
            total = total + self.courses[course]
            count = count + 1

        if count == 0:
            return 'GPA of student ' + self.name + ' is 0.0'
        else:
            return 'GPA of student ' + self.name + ' is ' + str(total / count)

    # this will list passed courses with using for-loop
    def displayCourses(self):
        passed = []
        for course in self.courses:
            if self.courses[course] > 0.0:
                passed.append(course)
        return passed


# this is the main part of the program
if __name__ == '__main__':
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    student2 = Student('Jessica', 123456)  # passed as int. handled in class

    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())
