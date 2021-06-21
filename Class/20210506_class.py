'''
class Car :
    color = ""
    speed = 0

    def __init__(self) :
        self.color = "빨강"
        self.speed = 0
     
    def upspeed(self, value) :
        self.speed += value

    def downspeed(self, value) :
        self.speed -= value
'''

# 인스턴스 (객체생성) 생성 : 실제 자동차를 만든다 생각 
'''
mycar1 = Car()               #자동차1 (인스턴스) 생성
mycar1.color = "빨강"
mycar1.speed = 0

mycar2 = Car()               #자동차2 (인스턴스) 생성
mycar2.color = "파랑"
mycar2.speed = 0

mycar3 = Car()               #자동차3 (인스턴스) 생성
mycar3.color = "노랑"
mycar3.speed = 0

#자동차 1 스피드 30증가
mycar1.upspeed(30)
print("자동차1의 색상은 %s이며, 현재 속도는 %dkm입니다." %(mycar1.color, mycar1.speed))

#자동차 2 스피드 60 감소
mycar2.downspeed(60)
print("자동차1의 색상은 %s이며, 현재 속도는 %dkm입니다." %(mycar2.color, mycar2.speed))

#자동차3 스피드 10감소
mycar3.downspeed(10)
print("자동차1의 색상은 %s이며, 현재 속도는 %dkm입니다." %(mycar3.color, mycar3.speed))
'''

# 생성자
#__init__ 이란 함수ㅡㄹ 생성자라 함.
'''
mycar1 = Car()
mycar2 = Car()

print("자동차1의 색상은 %s이며, 현재 속도는 %dkm입니다. " %(mycar1.color, mycar1.speed))
print("자동차2의 색상은 %s이며, 현재 속도는 %dkm입니다. " %(mycar2.color, mycar2.speed))
'''

#위에꺼 2번째
'''
class Car :
    color = " "  # 선언 안해도 상관없음
    speed = 0

    def __init__ (self, value1, value2) :
        self.color = value1
        self.speed = value2

mycar1 = Car("빨강", 30)
mycar2 = Car("노랑", 60)
print("자동차1의 색상은 %s이며, 현재 속도는 %dkm입니다. " %(mycar1.color, mycar1.speed))
print("자동차2의 색상은 %s이며, 현재 속도는 %dkm입니다. " %(mycar2.color, mycar2.speed))
'''

#인스턴스 변수와 클래스 변수
'''
class Car :
    count = 0

    def __init__(self) :
        self.speed = 0
        Car.count += 1

mycar1 = Car()
mycar1.speed = 30
print("자동차1의 현재  속도는 %4dkm 이고, 생산된 자동차는 %d입니다. " %(mycar1.speed, Car.count))
# print("자동차1의 현재  속도는 %dkm 이고, 생산된 자동차는 %d입니다. " %(mycar1.speed, mycar.count))

mycar2 = Car()
mycar2.speed = 60
print("자동차2의 현재  속도는 %4dkm 이고, 생산된 자동차는 %d입니다. " %(mycar2.speed, Car.count))

mycar3 = Car()
mycar3.speed = 100
print("자동차3의 현재  속도는 %3dkm 이고, 생산된 자동차는 %d입니다. " %(mycar3.speed, Car.count))
'''

# 메서드 오버라이딩
class Car:
    speed = 0
    def upspeed(self, value) :
        self.speed += value
        print("현재 속도(sedan 클래스) : %d"   %self.speed)
class Sedan(Car) :
    self.speed += value 
    if self.speed > 150 :
            self.speed = 150
    print("현재 속도(sedan 클래스) : %d"   %self.speed)

    def getseat(self) :
        return self.seat

class Truck(Car) :
    freight = 1000

    def getfrg(self) :
        return self.freight

truck1 = Truck()
sedan1 = Sedan()



