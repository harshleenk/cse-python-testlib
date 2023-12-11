class Library:
    def setname(self,name):
        self.name=name
    def getname(self):
        print(self.name)

class Staff(Library):
    def setId(self,Id):
        self.Id=Id
    def getId(self):
        print(self.Id)

class Student(Staff):
    def setcourse(self,course):
        self.course=course
    def getcourse(self):
        print(self.course)

name=input("name: ")
id=input("id: ")
course=input("course: ")

uni=Student()
uni.setname(name)
uni.setId(id)
uni.setcourse(course)

uni.getname()
uni.getId()
uni.getcourse()