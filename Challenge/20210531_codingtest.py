########################################
#  학번 :30120     이름:이화준
########################################
# 화일을 학번 이름으로 먼저 저장하세요. 예) 30129김상일

# <문제 1> 
#   - 숫자 5개를 입력받고 입력 받은 수 중에서 가장 큰 수를 출력하세요.
#   - 숫자 5개를 입력받는 부분은 for 반복문으로 작성하세요.

maxnum = 0
for i in range(5) :
    a = int(input("숫자를 입력해주세요 : "))
    if a > maxnum :
        maxnum = a
    
print(maxnum)

print('--'*45)

# <문제 2>
# 1. 생년월일을 다음과 같이 8자리로 입력 받는다.
#   예) 20031127
#      
# 2. 입력 받은 생년월일을 다음과 같이 처리해서 출력한다.
#  예)  2003년 11월 27일

birth = input("생년월일을 8자리로 입력해주세요 : ")

year = birth[0:4]
month = birth[4:6]
day = birth[6:8]

print("%s년 %s월 %s일" %(year, month, day))

print('--'*45)

# <문제 3> 
#   - 다음 조건을 만족하는 프로그램을 작성하세요.
#     - 무한 반복되는 while 문을 사용한다.
#     - 두 수를 입력 받아서 두 수가 같으면 break 문을 사용해 무한 반복문을 종료한다.

d = 1
while d == 1 :
    b= int(input("첫번째 정수를 입력해주세요 : "))
    c= int(input("두번째 정수를 입력해주세요 : "))
    print("첫번째 : %3d         두번째 : %3d" %(b, c))
    if b == c :
        print("입력하신 두 정수가 동일하여 반복을 종료합니다.")
        break

print('--'*45)

# <문제 4> 
#   - 다음 조건을 만족하는 프로그램을 작성하세요.
#    - 1부터 50까지의 수를 출력한다. 단, 3의 배수는 출력하지 않는다.
e = 1
for x in range(50) :
    if e % 3 != 0 :
        print(e)
    e = e + 1
    




