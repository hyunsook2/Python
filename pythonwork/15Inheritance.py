class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
        

x=Person('현석','김')
x.printname()

class Member(Person):
    def __init__(self, fname, lname, grade):
        super().__init__(fname, lname)
        self.grade=grade
        
    def welcome(self):
        print("welcome",self.firstname,self.lastname,self.grade)
        
    def printname(self):
        print(self.firstname,self.lastname,self.grade)
              

x=Member('Mike','Tom','VIP')
x.printname()