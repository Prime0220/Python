# #### [ 도전 문제 22 ] #### #
#
#       평년일 때 1, 3, 5, 7, 8, 10, 12월은 31일, 4, 6, 9, 11월은 30일, 2월은 28일이다. 월을 나타내는 숫자를
#       입력하면 그 달의 날짜 수를 반환하는 함수 days1를 만든다. 사용 예는 다음과 같다.
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
