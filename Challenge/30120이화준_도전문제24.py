# #### [ 도전 문제 24 ] #### #
#
#   3개의 숫자를 입력하면 " 그 숫자들의 합" 과 "그 숫자들을 제곱한 숫자들의 합"의 차이(큰 수에서 작은 수를 뺀값)를 계산하는 
#   함수 diffsum을 만든다. 큰 수에서 작은 수를 뺀 결과이므로 항상 0보다 크거나 같아야 한다.

def diffsum (a, b, c) :
    addsum = a + b + c
    mltplsum = a ** 2 + b ** 2 + c ** 2
    diff = addsum - mltplsum
    return abs(diff)

a, b, c = map(int, input("공백을 기준으로 정수 3개를 입력해주세요 : ").split(' '))
print("입력하신 정수 3개를 각각 제곱한 값의 차 : ", diffsum(a,b,c))
