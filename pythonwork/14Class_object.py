class Car:
    #속성
    engineCc=0
    door=0
    carType=None
    
    #생성자
    def __init__(파라미터ㅋㅋ,engineCc,door,carType):
        #멤버변수 초기화
        파라미터ㅋㅋ.engineCc=engineCc
        파라미터ㅋㅋ.door=door
        파라미터ㅋㅋ.carType=carType
        
    #Method
    def display(파라미터ㅋㅋ):
        print("차는 %d cc이고, 문은 %d개, 타입은 %s"%(파라미터ㅋㅋ.engineCc,파라미터ㅋㅋ.door,파라미터ㅋㅋ.carType))
            
car1 = Car(3000,4,'suv')
car2 = Car(5000,2,'truck')

car1.display()
car2.display()
    