class StName:
    def setname(self,name):
        self.name=name
    def getname(self):
        print(self.name)
class StInfo:
    def setschl(self,schl):
        self.schl=schl
    def getschl(self):
        print(self.schl)
class Student(StName,StInfo):
    def setaddress(self,address):
        self.address=address
    def getaddress(self):
        print(self.address)

obj=Student()
obj.setname("Harshi")
obj.setschl("MGN")
obj.setaddress("Jalandhar")
obj.getname()
obj.getschl()
obj.getaddress()