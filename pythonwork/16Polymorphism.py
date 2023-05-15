class Char:
    def __init__(self,name):
        self.name=name
    def do(self):
        print("do")
        
class Fighter(Char):
    def do(self):
        print("fighting")
        
class Healer(Char):
    def do(self):
        print("healing")
        
class Wizerd(Char):
    def do(self):
        print("casting") 

fingter1 = Fighter('hojin')
healer1 = Healer('rem')
wizard1 = Wizerd('Emilya')

for x in ( fingter1,healer1,wizard1 ):
    print(x.name, end=' ')
    x.do()