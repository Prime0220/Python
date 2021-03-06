#   {}안에 값의 순서를 지정하는 숫자를 넣을 수도 있다. 가장 앞에 있는 값은 {0}, 그 뒤의 값은 {1}, 이런 식으로 지정한다.
#   이 방법을 사용하면 값의 순서르 바꾸거나 같은 값을 여러번 인쇄할 수도 있다.

print("{2}의 {0} 점수는 {1}점입니다. {1}점! {1}점! ".format("수학", 100, "철수"))

print("\n", '--' * 45, "\n")

#   format 방식에서 공백의 크기를 지정하거나 부동소수점의 소수점 아래 숫자를 지정하 때는 {}안에 : 기호를 넣고
#   그 뒤에 고급 형식지정 문자열을 넣는다. : 뒤에 오는 숫자는 공백의 크기를 뜻한다. <는 값을 앞쪽으로 붙이고 공백을 
#   뒤로 붙인다. 반대로 >는 값을 앞쪽으로 붙이고 공백을 뒤로 붙인다. 소숫점의 자릿수를 지정하 때는 . 과숫자, 그리고 f 글자
#   를 사용한다.  , 기호를 넣으면 영미권에서 숫자르 쓸 때 천(1000)단위마다 붙이는 쉼표(thousand comma)를 붙인다.

#   고급 형식 지정 문자열    의미
#       {:10}       전체 10칸을 차지
#       {:>10}     전체 10칸을 차지하며 공백을 앞에 붙임
#       {:<10}     전체 10칸을 차지하며 공백을 뒤에 붙임
#       {:.5f}       부동소수점의 소수점 아래 5자리까지 표시
#       {:,}          천단위 쉼표 표시

# 표 3.2.2 : format 방식의 고급 형식지정 문자여

print("[{:<20}]".format("*"))

print("[{:>20}]".format("20"))

print("[{:20.5f}]".format(1 / 3))

print("[{:20,}]".format(1234567890))

print("\n", '--' * 45, "\n")

# #### [ 연습문제 2 ] #### #
# 1. a, b 두 개의 변수에 3과 12 라는 값을 넣고 이 변수를 사용하여 다음과 같이 세로셈으로 곱셈 결과를 출력하는 코드를
#     만들어라.


#                       3
#           x         12
#           -----------
#                      36

#   1번

a = 3
b = 12
print("{:>8}".format(a))
print("x{:>6}".format(b))
print('─' * 3)
print("{:>7}".format(a*b))

print("\n", '--' * 45, "\n")

# 2. a, b 두 개의 변수에 "123456"과 "7890" 라는 값을 넣고 이 변수를 사용하여 다음과 같이 세로셈으로 덧셈 결과를 출력하는
#    코드를 만들어라. 천의 자리 쉼표를 표시해야 한다.

#              123,456
#           +     7,890
#           -----------
#              131,346

#   2번 

c = 123456
d = 7890


print("{:10,}".format(c))
print("+{:9,}".format(d))
print("─" * 5)
print("{:>10,}".format(c + d))

print("\n", '--' * 45, "\n")

# # 파이썬 함수 # #

#   함수(function)는 입력(input)을 받으면 그 입력에 해당하는 출력(output)을 반환(return)하는 기계와 같다. 
#   예를 들어 500원을 넣으면 생수가 나오고, 1000원을 넣으면 콜라가 나오는 자판기는 다음과 같은 함수이다.

#   f(500) = "생수"
#   f(1000) = "콜라"

#   파이썬에는 def키워드를 사용하여 다음과 같이 함수르 만들 수 있다.

#   def 함수이름(입력변수이름) :
#       출력변수를 만드는 명령
#       return 출력변수이름

#   def키워드는 영어로 "정의한다"는 의미를 가지는 define에서 만들어졌다.

#   예를 들어 숫자 x를 입력하면 두 배가 되도록 하는 함수는 다음과 같다.

def twotimes(x) :
    y = 2 * x
    return y

x = int(input("숫자를 입력해주세요 : "))
print(twotimes(x))

print("\n", '--' * 45, "\n")

#   이렇게 만들어진 함수를 사용하려면 함수 이름과 그 뒤에 괄호로 싸인 입력값을 넣으면 된다.

e = twotimes(2)
print(a)

print("\n", '--' * 45, "\n")

f = twotimes(10)
print(b)

print("\n", '--' * 45, "\n")

# #### [ 도전 문제 1 ] #### #
#
#   1. 짝수가 입력되면 "짝수"라는 문자열을, 홀수가 입력되면 "홀수"라는 문자열을 반환하는 함수를 만든다.
#   2. 윤년을 나타나는 수가 입력되면 "윤년"이라는 문자열을, 그렇지 않은 수가 입력되면 "평년"이라는 문자열을 
#       반환하는 함수를 만든다.

def Num(num) :

    if num % 2 == 1 :
        numName = "홀수입니다. "
    else :
        numName = "짝수입니다. "
    return numName

num = int(input("숫자를 입력해주세요 : "))
print(Num(num))

print("\n", '--' * 45, "\n")

# #### [ 도전문제 2 ] #### #
#
#   평년일 때 1, 3, 5, 7, 8, 10, 12월은 31일, 4, 6, 9, 11월은 30일, 2월은 28일이다. 월을 나타내는 숫자를
#    입력하면 그 달의 날짜 수를 반환하는 함수 days1를 만든다. 사용 예는 다음과 같다.
#
#   print(days1(11))
#   30

def days1(mon) :
    Day31 = {1, 3, 5, 7, 8, 10, 12}
    Day30 = {4, 6, 9, 11}
    if mon in Day31 :
        day = 31
    elif mon in Day30 :
        day = 30
    elif mon == 2 :
        day = 28
    else :
        print("잘못 입력하셨습니다.")
        day = 0
    return day


for i in range(13) :
    mon = int(input("몇월인지 입력해주세요 : "))
    print(days1(mon))






