Day31 = {1, 3, 5, 7, 8, 10, 12}
Day30 = {4, 6, 9, 11}

def days2(yearmon) :
    year = int(yearmon[0:4])
    mon = int(yearmon[4:6])
    if mon in Day31 :
        day = 31
    elif mon in Day30 :
        day = 30
    else :
        if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) :
            day = 29
        else :
            day = 28
    return day

yearmon = input("공백을 기준으로 몇년 몇월인지 입력해주세요 : ")
print(days2(yearmon))
