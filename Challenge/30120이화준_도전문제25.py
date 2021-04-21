# #### [ 도전 문제 25] #### #
#
#   함수 바깥에 m 이라는 전역 변수를 만들고 그 값을 0으로 놓는다.
#   앞에서 만든 diffsum 함수를 고쳐서 diffsum 함수와 같은 값을 반환하지만 함수를 실행할 때 마다
#   diffsum 함에서 계산된 값이 원래 있던 m보다 크면 m을 계산된 값으로 바꾸는 함수 diffsum2 를 만든다.

def diffsum2(a, b, c) :
    global m
    addsum = a + b + c
    mltplsum = a ** 2 + b ** 2 + c ** 2
    diff = addsum - mltplsum

    if diff > m :
        m = diff
      
    return abs(diff)

a, b, c = map(int, input("공백을 기준으로 정수 3개를 입력해주세요 : ").split(' '))

print("입력하신 정수 3개를 각각 제곱한 값의 차 : ", diffsum2(a,b,c))
print("입력하신 정수의 값중 가장 큰 값 : ", m)

    
