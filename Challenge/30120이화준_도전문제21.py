###### [ 도전문제 21 ] ######
#
#    1. 짝수가 입력되면 " 짝수 "라는 문자열을, 
#        홀수가 입력되면 " 홀수 "라는 문자여을 
#        반환하는 함수를 만든다.
#

def numchk(a) :
    if a % 2 == 0 :
        str_ = "짝수입니다."
    else :
        str_ = "홀수입니다."
    return str_

a = int(input("정수를 입력해주세요 : "))

print(numchk(a))

print('--' * 45 )

#       2. 윤년을 나타내는 수가 입력되면 " 윤년 "이라는 문자열을
#           그렇지 않은 수가 입력되면 " 평년 "이라는 문자열을 반환하는 함수를 만든다.

def Yearchk(year) :
    if year % 4 == 0 :
        yearname = "윤년입니다. "
    else :
        yearname = "평년입니다. "
    return yearname

year = int(input("년도를 입력해 주세요 (ex : 2004): "))

print(Yearchk(year))

